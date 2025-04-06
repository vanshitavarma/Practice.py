'''def _prime(n):
    if n==0 or n<0 or n==1:
        return None
    elif n==2:
        return True 
    else:
        for i in range(2,n):
            if n%i==0:
                return False
            else:
                return True

x=int(input("enter the number:"))
if _prime(x):
    print(f'{x}is a prime number')
elif _prime(x)is None:
    print("It is either invalid input or the number is neither prime nor composite")
else:
    print(f'{x}is not a prime number')'''
    
def _prime(n):
    if n==0 or n<0 or n==1:
        return None
    elif n==2:
        return True
    else:
        for i in range(2,n):
            if n%i==0:
                return False
            else:
                return True
x=int(input("Enter The Number: "))
if _prime(x):
    print(f'{x} is a prime number')
elif _prime(x)is None:
    print("It is neither a prime nor a composite or it is a invalid input")
else:
    print(f'{x} is not a prime number')
