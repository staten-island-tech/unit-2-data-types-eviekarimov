import random
number = random.choice (1,2,3,4,5,6,7,8,9,10)
(x) = int(input("Guess: "))
if (x) == number:
    print("correct")
elif x < number:
        print("try again; its greater")
        int(input(input guess again))
               
        print("greater")
elif x > number:
        print("try again; its smaller")
        int(input("guess again"))
    
  
