def firstMethod():
    secondMethod()
    print("Calling First Method..")

def secondMethod():
    thirdMethod()
    print("Calling Second Method..")

def thirdMethod():
    fourthMethod()
    print("Calling Third Method..")

def fourthMethod():
    print("Calling Fourth Method")

firstMethod()