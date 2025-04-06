#write a program to count a vowel in a string
def count_vowels(s):
    vowels = "aeiouAEIOU"
    vowel = 0
    for char in s:
        if char in vowels:
            vowel += 1
    return vowel

a = "vanshita"
result = count_vowels(a)
print(f"Number of vowels in {a}: {result}")
