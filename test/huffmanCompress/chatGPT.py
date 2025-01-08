import heapq
from collections import defaultdict

class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

def build_huffman_tree(data):
    frequency = defaultdict(int)
    for char in data:
        frequency[char] += 1

    priority_queue = [Node(char, freq) for char, freq in frequency.items()]
    heapq.heapify(priority_queue)

    while len(priority_queue) > 1:
        left_child = heapq.heappop(priority_queue)
        right_child = heapq.heappop(priority_queue)

        internal_node = Node(None, left_child.freq + right_child.freq)
        internal_node.left = left_child
        internal_node.right = right_child

        heapq.heappush(priority_queue, internal_node)

    return priority_queue[0]

def generate_huffman_codes(root, current_code="", codes={}):
    if root:
        if root.char is not None:
            codes[root.char] = current_code
        generate_huffman_codes(root.left, current_code + "0", codes)
        generate_huffman_codes(root.right, current_code + "1", codes)

def compress(data):
    root = build_huffman_tree(data)
    codes = {}
    generate_huffman_codes(root, "", codes)
    compressed_data = "".join(codes[char] for char in data)
    return compressed_data, root

def decompress(compressed_data, root):
    current_node = root
    decompressed_data = ""

    for bit in compressed_data:
        if bit == "0":
            current_node = current_node.left
        else:
            current_node = current_node.right

        if current_node.char is not None:
            decompressed_data += current_node.char
            current_node = root

    return decompressed_data

# Example usage:
input_data = "this is an example for huffman encoding"
compressed_data, huffman_tree_root = compress(input_data)
print(f"Original data: {input_data}")
print(f"Compressed data: {compressed_data}")

decompressed_data = decompress(compressed_data, huffman_tree_root)
print(f"Decompressed data: {decompressed_data}")
