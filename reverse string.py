def toFar(t):
    return ((t*(9/5))+32)

def toCel(t):
    return ((t-32)*(5/9))

    
print("----Menu----\n")
print('1.Cel to far\n')
print('2.Far to cel\n')

choice=int(input("Enter your choice:"))
temp=float(input("Enter the temperature:"))     

match choice:
        case 1:  print(f'Temperature in far:{toFar(temp)}')
      

        case 2: print(f'Temperature in far:{toCel(temp)}')
       
        
        case _:("invalid input\n")
     


temp=float(input("Enter the temperature:"))
