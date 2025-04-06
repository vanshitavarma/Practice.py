#WRITE A PROGRAM TO CONVERT CELSIUS TO FAHRENHEIT
def celsius_fahrenheit(c):
  f=(9*c/5)+32
  return f

c=int(input("ENTER THE TEMPREATURE IN DEGREE: "))
f=celsius_fahrenheit(c)
print(f"the tempreature in {c} degree is {f} fahrenheit")
