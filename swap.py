#WRITE A PROGRAM TO SWAP TWO VARIABLES
def swap(a,b):
    a,b=b,a
    return a,b
x=int(input("enter the value of x:"))
y=int(input("enter the value of y:"))
swap(x,y)
print(f" After swapping x is {y} and y is {x}")
