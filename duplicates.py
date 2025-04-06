#write a program to remove duplicates from list
def remove_duplicates(l):
     return list(set(l))
numbers=list(map(int,input("ENTER NUMBERS SEPERATED BY SPACES: ").split()))
s=remove_duplicates(numbers)
print("Lists after removing duplicates: ",s)
                      
