#WRITE A PROGRAM TO FIND LARGEST AND SMALLEST NUMBER IN A LIST
def largest_smallest(n):
    smallest=min(n)
    largest=max(n)
    return smallest,largest
n=list(map(int,input("ENTER THE NUMBER SEPERATED BY COMMAS").split(',')))
smallest,largest=largest_smallest(n)
print(f"Smallest number:{smallest}")
print(f"Largest number:{largest}")
        

