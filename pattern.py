rows=int(input("Enter the no.of rows"))
for i in range(1, rows+1):
    print(" "*(rows-i),end=" ")
    print("*"*(2*i-1))
for i in range(1, rows-1):
    print(" "*(rows+i),end=" ")
    print("*"*(2*i+1))
    #print(" "*(rows-i),end=" ")


