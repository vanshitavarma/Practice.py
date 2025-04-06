x=int(input("enter value of x: "))
match x:
    case 0:
        print("x is zero")
    case _ if  x!=90:
         print(x, "is not 90")
          
        