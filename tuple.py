# 23. Write a Python program to create a tuple and print its elements.
'''
num = int(input("enter the no. of elements you want to insert in tuple: "))
l=[]
for i in range(num):
    ele=int(input(f"enter element {i+1}: "))
    l.append(ele)
t=tuple(l)
print(t)
'''   
        
# 24. Write a program to find the length of a tuple.
'''
t=(10,29,38)
print(len(t))
'''
'''
t=(10,29,38)
count=0
for i in t:
    count+=1
print(count)
'''

# 25. Write a program to find the maximum and minimum element in a tuple.
'''
t=(10,29,38)
temp=t[0]
mini=t[0]
for i in range(len(t)):
    if temp < t[i]:
        temp = t[i]
    if mini > t[i]:
        mini=t[i]
print("the maximum element in the tuple is",temp)
print("the minimum element in the tuple is",mini)
'''

# 26. Write a program to convert a tuple into a list.
'''
t=(10,29,38)
x=list(t)
print(x)
'''

# 27. Write a program to check if an element exists in a tuple.
'''
t=(10,29,38)
num=int(input("enter a no.: "))
if num in t:
    print("exists")
else:
    print("does not exists")
'''

# 28. Write a program to count occurrences of an element in a tuple.
'''
t = (10,29,38,29,10)
num = int(input("Enter element: "))
print(t.count(num))
'''

# 29. Write a program to slice a tuple and display the result.
'''
t=(10,29,38,40)
print(t[1:3])
'''
# 30. Write a program to find repeated elements in a tuple.
'''
t=(10,29,38,29,10)
u=[]
for i in t:
    if i not in u:
        u.append(i)
    else:
        print(i)
'''

# 31. Write a program to merge two tuples.
'''
t=(1,2)
x=(3,5)
y=t+x
print(y)
'''

# 32. Write a program to unpack elements of a tuple into variables.
'''
t = (10, 20, 30)
a, b, c = t
print(a, b, c)
'''

# 33. Write a Python program to sort a tuple.
'''
t=(10,5,15,1)
l=list(t)
l.sort()
x=tuple(l)
print(x)
'''

# 34. Write a program to convert a list of tuples into a dictionary.
'''
l=[(1,2),(10,20),(30,40)]
d=dict(l)
print(d)
'''

# Advanced Level

# 35. Write a program to find the index of an element in a tuple.
'''
t=(10,5,15,1)
print(t.index(10))
'''

# 36. Write a program to remove an element from a tuple (without directly modifying it).
'''
t=(10,5,15,1)
x=[]
r=1
for i in t:
    if i != r:
        x.append(i)
y=tuple(x)
print(y)
'''       

# 37. Write a program to find common elements between two tuples.
'''
a=(10,20,30)
b=(40,50,20)
for i in a:
    if i in b:
        print(i)
'''

# 38. Write a Python program to check if a tuple is a palindrome.
'''
a=(10,20,10)
b=a[::-1]
if a == b:
    print("palindrome")
else:
    print("not palindrome")
'''

# 39. Write a program to find the element with maximum frequency in a tuple.
'''
a=(10,20,10,10,20,30)
ans=[]
b=[]
for i in a:
    if i not in b:
        b.append(i)
for i in b:
    ans.append([i,a.count(i)])
max_freq = 0
element = None
for i in ans:
    if i[1] > max_freq:
        max_freq = i[1]
        element = i[0]
print("Element with maximum frequency:", element)
print("Frequency:", max_freq)
'''
        
# 40. Write a program to create a nested tuple and access its elements.
'''
a=((10,20),(30,40))
for i in a:
    for j in range(len(i)):
        print(i[j])
'''






























