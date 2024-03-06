import random
num = random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
y = ('Incorrect')
incorrectanswers = []

while y == ('Incorrect'):
    x = int(input("Number:"))
    if (x) == (num):
        print('correct')
        y = ('Correct')

    else:
        incorrectanswers.append(x)
        if x < num:
            print("go again, numby is bigger")
        if x > num:
            print("go again: numby is less")

        print(incorrectanswers)

"""if x > number:
    x == ("incorrect")
    print("It's smaller; try again")
        
if x < number: 
    x == ("incorrect")
    print("Its bigger; try again")

else: 
    print("yes")


while x == ("incorrect"):
    (x) = int(input("Guess again:")) this is wrong"""

       


