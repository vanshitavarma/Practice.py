n=int(input("ENTER THE NUMBER OF ROWS"))
#half triangle
print("HALF TRIANGLE")
for i in range(n):
    for j in range(i):
        print('*',end=" ")
    print()


n=int(input("ENTER THE NUMBER OF ROWS"))
#half triangle
print(" RIGHT SIDE HALF TRIANGLE")
for i in range(n):
    for j in range(n-i):
        print(' ',end="")
    for k in range (i):
        print("*",end="")
    print()

n=int(input("ENTER THE NUMBER OF ROWS"))
#half triangle
print(" HALF lower TRIANGLE")
for i in range(n):
    for j in range(n-i):
        print('*',end=" ")
    print()

    
n=int(input("ENTER THE NUMBER OF ROWS"))
#half triangle
print(" RIGHT SIDE HALF LOWER  TRIANGLE")
for i in range(n):
    for j in range(i):
        print(' ',end=" ")
    for k in range (n-i):
        print("*",end=" ")
    print()



n=int(input("ENTER THE NUMBER OF ROWS"))
print("TRIANGLE")
for i in range(n):
    for j in range(n-i):
        print(' ',end="")
    for k in range(2*i-1):
        print("*",end="")
    print()
for i in range(n):
    for j in range(i):
        print(' ',end="")
    for k in range(2*(n-i)-1):
        print("*",end="")
    print("")

n=int(input("ENTER THE NUMBER OF ROWS"))
#half triangle
print(" ABC HALF TRIANGLE")
for i in range(n):
    for j in range(i):
        print(int(1+j),end=" ")
    print()

n=int(input("ENTER THE NUMBER OF ROWS"))
#half triangle
print(" RIGHT SIDE HALF TRIANGLE")
for i in range(n):
    for j in range(n-i):
        print(' ',end="")
    for k in range (i):
        print(chr(65+k),end="")
    print()

n=int(input("ENTER THE NUMBER OF ROWS"))
#half triangle
print(" HALF lower TRIANGLE")
for i in range(n):
    for j in range(n-i):
        print(chr(65+j),end=" ")
    print()

    
n=int(input("ENTER THE NUMBER OF ROWS"))
#half triangle
print(" RIGHT SIDE HALF LOWER  TRIANGLE")
for i in range(n):
    for j in range(i):
        print(' ',end=" ")
    for k in range (n-i):
        print(chr(65+k),end=" ")
    print()



n=int(input("ENTER THE NUMBER OF ROWS"))
print("TRIANGLE")
for i in range(n):
    for j in range(n-i):
        print(' ',end="")
    for k in range(2*i-1):
        print(chr(65+k),end="")
    print()
for i in range(n):
    for j in range(i):
        print(' ',end="")
    for k in range(2*(n-i)-1):
        print(chr(65+k),end="")
    print("")


