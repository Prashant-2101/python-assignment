# Basic

# 1. Create a set and add elements dynamically.
'''
s=set()
num=int(input("no. of elements: "))
for i in range(num):
    x=input(f"element {i+1}: ")
    s.add(x)
print("set is",s)
'''

# 2. Find the union and intersection of two sets.
'''
a={10,29,38}
b={12,13,10}
print(a.union(b))
print(a.intersection(b))
'''

# 3. Remove duplicate elements from a list using a set.
'''
a=[10,20,10]
b=set(a)
print(b)
'''

# 4. Check if an element exists in a set.
'''
a={10,29,38}
num=int(input("enter a no.: "))
exist=False
for i in a:
    if i == num:
        exist=True
        break
if exist:
    print("element exists")
else:
    print("element does not exist")
'''

# 5. Find the difference between two sets.
'''
a={10,29,38}
b={12,13,10}
print(a.difference(b))
'''

# Intermediate

# 6. Find common elements in two lists using sets.
'''
a = [10, 29, 38]
b = [12, 13, 10]

result = list(set(a) & set(b))

print("Common elements:", result)
'''

# 7. Check whether one set is a subset of another.
""""
a={10,29,38}
b={12,13,10}
print(a.issubset(b))
"""

# 8. Find symmetric difference of two sets.
'''
a={10,29,38}
b={12,13,10}
print(a.symmetric_difference(b))
'''

# 9. Count unique elements in a list using a set.
'''
a=[10,20,10,30]
b=set(a)
print(len(b))
'''

# 10. Remove all common elements from two sets.
'''
a = {10, 29, 38}
b = {12, 13, 10}

print(a.symmetric_difference(b))
'''

# Tricky

# 11. Find missing numbers from 1 to n using sets.
'''
n = int(input("enter n: "))

a = [1, 2, 4, 6]   

full_set = set(range(1, n+1))
given_set = set(a)

missing = full_set - given_set

print("Missing numbers:", missing)
'''

# 12. Check if two lists have any common elements.
'''
a = [10, 29, 38]
b = [12, 13, 10]
flag=False
for i in a:
    if i in b:
        flag=True
        break
if flag:
    print("common")
else:
    print("not common")
'''    
    

# 13. Convert a set of strings into uppercase.
'''
a = {"abc", "xyz"}

b = set()

for i in a:
    b.add(i.upper())

print(b)
'''

# 14. Identify unique vowels in a given string using a set.
'''
a="aaeiiou"
b=set(a)
print(b)
'''

# 15. Find elements that appear only once in a list.
'''
a = ["hello", "hi", "hi", "xyz"]

for i in a:
    if a.count(i) == 1:
        print(i)
'''
