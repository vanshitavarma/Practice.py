x=int(input("Enter a number: ")) 
fact=1 
if x<0: 
 print("Factorial does not exist for negative numbers") 
elif x==0: 
 print("The factorial of 0 is 1") 
else: 
 for i in range(1,x+1): 
  fact*=i 
 print("The factorial of ",x," is ",fact)
