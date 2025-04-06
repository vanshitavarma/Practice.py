'''
Write a program to capitalize the first letter of each word in a sentence.
IMPORT; re is not a built i module so gotta import it
r' is a raw string used to check special characters like punctuations and are treated literally
\w matches any non word character
matches more than one occurance
re.split syntax is (patern,text)
'''
import re
def capitalize_each_word(s):
    words=re.split(r'(\W+)', s)
    capitalized=[word.capitalize() if word.strip()and word.isalpha() else word for word in words]
    return "".join(capitalized)
s=input("ENTER THE STATEMENT:")
r=capitalize_each_word(s)
print(r)
    

