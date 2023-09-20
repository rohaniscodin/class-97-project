import random
number=random.randint(1,9)
y=number
while y ==number:
    monkey=input("Guess a number between 1 and 9")
    if monkey== number:
        print("You got it right")
        number=3
    else:
        print("Incorrect")