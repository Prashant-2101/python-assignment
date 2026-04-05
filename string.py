# Basic 
# 1. Write a program to count the number of vowels in a string.
'''
s="jai sri ram"
count=0
vowels="aeiou"
temp=[]
for i in s:
    if i in vowels:
        temp.append(i)
        count+=1
print(f"There are {count} vowels in the string which are {temp}")
'''


# 2. Reverse a string without using built-in functions.
'''
s="jai sri ram"
x=s[::-1]
print(x)
'''

# 3. Check whether a string is a palindrome.
"""
s="jai sri ram"
if s == s[::-1]:
    print("palindrome")
else:
    print("not palindrome")
"""

# 4. Count uppercase and lowercase letters in a string.
'''
s="Jai Sri Ram"
uc=[]
lc=[]
for i in s:
    if ord(i) in range(65,91):
        uc.append(i)
    if ord(i) in range(97,123) and i != " ":
        lc.append(i)
print(f"there are {len(uc)} uppercase letters in the string: ",uc)
print(f"there are {len(lc)} lowercase letters in the string: ",lc)
'''
        
# 5. Replace all spaces in a string with _.
"""
s="Jai Sri Ram"
p=s.replace(" ","_")
print(p)
"""   

# Intermediate

# 6. Find the frequency of each character in a string.
"""
s="Jai Sri Ram"
temp=[]
for i in s:
    if i not in temp:
        temp.append(i)
        print(f"frequency of {i} is {s.count(i)}")
"""

# 7. Remove duplicate characters from a string.
'''
s="Jai Sri Ram"
temp=[]
for i in s:
    if i not in temp:
        temp.append(i)
x="".join(temp)
print(x)
'''

# 8. Find the first non-repeating character in a string.
'''
s = "Jai Sri Ram"
for ch in s:
    if s.count(ch) == 1 and ch != " ":
        print(ch)
        break
'''

# 9. Check if two strings are anagrams.
'''
s1 = "ram"
s2 = "arm"

if len(s1) != len(s2):
    print("not anagram")
else:
    flag = True
    for ch in s1:
        if s1.count(ch) != s2.count(ch):
            flag = False
            break

    if flag:
        print("anagram")
    else:
        print("not anagram")
'''

# 10. Convert "hello world" → "Hello World" (title case without using .title()).
'''
s = "hello world"
words = s.split()
result = []
print(words)
for word in words:
    new_word = word[0].upper() + word[1:].lower()
    result.append(new_word)

print(" ".join(result))
'''  
        

# Tricky 
# 11. Find the longest word in a sentence.
'''
s= "I want to become a devotee of god Sri Ram."
words=s.split()
length=[]
for i in words:
    length.append(len(i))
maximum_length_index=length.index(max(length))
print(words[maximum_length_index])
'''   
        
# 12. Compress a string like "aaabbc" → "a3b2c1".
'''
s = "aaabbc"
temp = []
x = []

for ch in s:
    if ch not in temp:
        temp.append(ch)
        x.append(str(s.count(ch)))

result = ""
for i in range(len(temp)):
    result += temp[i] + x[i]

print(result)
'''
    
# 13. Count words, characters, and digits in a string.
'''
s = "Hello 123 World"

words = s.split()
print(words)

word_count = len(words)
character_count = len(s)

digit_count = 0
for i in s:
    if i.isdigit():
        digit_count += 1

print(f"there are {word_count} words in the string.")
print(f"there are {character_count} characters in the string.")
print(f"there are {digit_count} digits in the string.")
'''

# 14. Rotate a string left by n positions.
'''
s = "Hello 123 World"
l=[]
for i in s:
    l.append(i)

n= int(input("enter a natural number: "))
for i in range(n):
    l.insert(len(s),l[0])
    l.pop(0)
#print(l)
new_string="".join(l)
print("the string after rotating by n positions is:",new_string)
'''

# 15. Find all substrings of a given string.
'''
s = "Hello"
print(s)

l = []

for i in range(len(s)):
    for j in range(i + 1, len(s) + 1):
        l.append(s[i:j])

print(l)
'''


