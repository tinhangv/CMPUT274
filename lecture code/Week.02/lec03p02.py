theCount = 0
word = ""
while word != "exit":
    word = input("Word: ")
    if word == 'the':
        theCount = theCount + 1
    elif word == 'The':
        theCount = theCount + 1
    print( "Total count %s" % (theCount) )
