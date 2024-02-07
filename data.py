""" #data types, Numbers 1,2,3 etc.
def add(x,y):
    print(x + y)
add(45,35)

  #strings "a,b,c"
def message(name):
        print(name)
message("Agnes")
x="1"
int(x)
add("35","45")

#booleans
x = True

def check(x):
    if(x == True):
        print("is logged in")
    else:
        print("please login")
    check(x) """

 values = [1,2.23,5,7,2,30,15]
print(values)
for i in values:
    print(values[0]) #bracekts show position in list


#strings
x = "this is a thing"
y= x.split( ) 
z= y[0]
print(y)
print(z)

even_or_odd = int (input("integer"))
if (even_or_odd) == 0:



y=input("give me a sentence")
print(y)
y= y.split(" ")
print(len(y)) 


def get_all_factors(n):
   factors = []
   for i in range(1,n*1):
      if n%1 == 0:
         factors.append(i)
    return factors

number = int(input("please enter a number: ":))

