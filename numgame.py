import random
(x) = int(input("Guess: "))
number = random.choice([1,2,3,4,5,6,7,8,9,10])

if x > number:
    x == ("incorrect")
    print("It's smaller; try again")
        
if x < number: 
    x == ("incorrect")
    print("Its bigger; try again")

else: 
    print("yes")


while x == ("incorrect"):
    (x) = int(input("Guess again:"))

       


