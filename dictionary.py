'''n=input("Enter String:")
frequency={}
for char in n:
    if char in frequency:
        frequency[char]=frequency[char]+1
    else:
        frequency[char]=1
print(frequency)'''

'''dict1={"name1":"vanshita","roll no.of vanshita":"61"}
dict2={"name2":"dishita","roll no.of dishita":"62"}
dict1.update(dict2)
print(dict1)'''

'''def input_dict(n):
    print(f"Enter {n} key value pairs for dictionary:")
    user_dict={}
    for _ in range(n):
        key,value=input("Enter key and value seperated by space: ").split()
        user_dict[key]=value
    return user_dict
n1=int(input("enter the number of key-value pairs for dictionary 1: "))
dict1=input_dict(n1)
n2=int(input("enter the number of key-value pairs for dictionary 1: "))
dict2=input_dict(n2)

dict1.update(dict2)
print("MERGED DICTIONARY:",(dict1))'''


def input_dict(n):
    print(f"Enter {n}key value pairs for dictionary:")
    user_dict={}
    for i in range(n):
        key,value=input("Enter key and value seperated by space: ").split()
        user_dict[key]=value
    return user_dict

n1=int(input("enter the number of key-value pairs for dictionary 1: "))
dict1=input_dict(n1)

max_key = max(dict1)
print(f"Max key: {max_key}", f"Value: {dict1[max_key]}")



                 

