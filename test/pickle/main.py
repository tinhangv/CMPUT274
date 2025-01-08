import pickle

class Fruit:
    def __init__(self, name:str, calories: float):
        self.name = name
        self.calories = calories

    def describe_fruit(self):
        print(self.name, self.calories, sep=": ")

if __name__ == '__main__':
    # fruit: Fruit = Fruit('Banana', 100)
    # fruit.describe_fruit()
    # with open('data.pickle', 'wb') as file:
    #     pickle.dump(fruit, file)
    with open('data.pickle','rb') as file:
        fruit: Fruit = pickle.load(file)
    fruit.describe_fruit()
    fruit.calories += 200
    fruit.describe_fruit()

    with open('data.pickle', 'wb') as file:
        pickle.dump(fruit, file)
