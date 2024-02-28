import random
number = random.choice (1,2,3,4,5,6,7,8,9,10)
(x) = int(input("Guess: "))
while (x) != number:
    if x > number:
        print ("It's smellier; try again")
    if x < number: 
        print ("Its booger, try again")
        x = input "guess again"
else: 
        print ("you got it!")

