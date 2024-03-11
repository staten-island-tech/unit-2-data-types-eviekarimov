accounts = [["1", "2", "8"], ["4","5", "6"], ["7", "8", "9"]]
y = [{int(i) for i in x} for x in accounts]
print(y[0])

def max():
    z = sum(y[0])
    a = sum(y[1])
    b = sum(y[2])
    if z > a and z > b:
        print(z)
    elif a > z and a> b:
        print(a)
    elif b > a and b > z:
        print(b)
    else: 
         if z == a == b:
                print(z)
max()                                                                                                                                                                                                                                                                                                                                                                        