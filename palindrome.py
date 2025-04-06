def is_palindrome(s):
   s=s[::-1]
   return s

n=input("ENTER STRING: ")
s=is_palindrome(n)
if (n==s):
    print(f'{n} is a palindrome')
else:
    print(f'{n}it is not a palindrome')
