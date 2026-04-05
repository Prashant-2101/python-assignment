# LIST

# 1. Write a Python program to create a list of integers and print its elements.
'''
a=[]
num=int(input("how many numbers do you want to insert in the list: "))
i=1
while i <= num:
    element=int(input(f"enter element {i}: ")) 
    a.append(element)
    i+=1
print(a)
'''

# 2. Write a program to find the sum and average of all elements in a list.
'''
a=[10,20,30]
total=0
for i in range(3):
    total+=a[i]
avg=total/3
print("total is",total)
print("average is",avg)
'''

# 3. Write a program to find the largest and smallest element in a list.
'''
a=[]
num=int(input("how many numbers do you want to insert in the list: "))
i=1
while i <= num:
    element=int(input(f"enter element {i}: ")) 
    a.append(element)
    i+=1
print(a)
largest=a[0]
smallest=a[0]
for j in a:
    if j > largest:
        largest = j
    if j < smallest:
        smallest = j
print(f"the largest element in the list is {largest}.")
print(f"the smallest element in the list is {smallest}.")
'''

# 4. Write a Python program to count the number of elements in a list without using len().
'''
a=[12,98,67]
count=0
for i in a:
    count+=1
print("the number of elements in a list:",count)
'''

# 5. Write a program to reverse a list without using built-in functions.
"""
a=[12,98,67]
b=[]
count=0
for i in a:
    count+=1
while count>0:
    b.append(a[count-1])
    count-=1
print("the reverse of the list is:",b)
"""
'''
a=[12,98,67]
a=a[::-1]
print(a)
'''

# 6. Write a program to check if an element exists in a list.
'''
a=[12,98,67]
num=int(input("enter a number: "))
for i in a:
    if i == num:
        print(f"{num} exists in the list.")
        break
else:
    print(f"{num} does not exist in the list.")
'''

# 7. Write a Python program to remove duplicate elements from a list.
'''
d=[10,20,10,30,20]
x=[]
for i in d:
    if i not in x:
        x.append(i)
print(x)
'''

# 8. Write a program to sort a list in ascending and descending order.
'''
a=[12,56,34]
a.sort()
print("the ascending order of the list is",a)
a.sort(reverse=True)
print("the descending order of the list is",a)
'''

# 9. Write a program to merge two lists and remove duplicates.
'''
a=[12,34,56]
b=[78,56]
a.extend(b)
print("the list after merging the two lists",a)
c=[]
for i in a:
    if i not in c:
        c.append(i)
print("the list after removing duplicates is",c)
'''

# 10. Write a program to find common elements between two lists.
'''
a=[12,34,56]
b=[78,56]
for i in a:
    if i in b:
        print("common elements between two lists:",i)
'''

# 11. Write a program to split a list into even and odd numbers.
'''
a=[1,2,3,4]
even = []
odd = []

for i in a:
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)
print(even)
print(odd)
'''

# 12. Write a program to rotate a list by n positions.
'''
a=[1,2,3,4]
n = int(input("enter the no. of positions: "))
for i in range(n):
    a.insert(0,a[-1])
    a.pop()
print(a)
'''

# 13. Write a Python program to find the second largest number in a list.
'''
a = [10,29,38,56,47]
a.sort()
print("the second largest number in the list is",a[-2])
'''

# 14.  Write a program to flatten a nested list.
'''
a = [[1,2], [3,4], [5,6]]
flat = []
for i in a:
    for j in i:
        flat.append(j)
print(flat)
'''

# 15. Write a program to count frequency of each element in a list.
'''
a = [10,29,38,56,47,38]
for i in a:
    print(f"frequency of {i} is {a.count(i)} in the list.")
'''

# 16. Write a program to replace all negative numbers with zero in a list.
'''
a=[-1,-2,3]
for i in a:
    if i < 0:
        a[a.index(i)]=0
print("the list after replacing all negative numbers with zero:",a)
'''

# 17. Write a program to remove all occurrences of a given element from a list.
'''
a = [10,29,38,56,47,38]
a = [i for i in a if i != 38]
print(a)
'''

# 18. Write a program to check if a list is a palindrome.
#a = [10,29,38,56,47,38]
'''
a = [10,20,10]
if a == a[::-1]:
    print("the list is a palindrome")
else:
    print("the list is not a palindrome")
'''

# 19. Write a Python program to find missing numbers in a given list of consecutive integers.
'''
a=[1,2,3,5,6,8]
missing=[]
for i in range(a[0],a[-1]):
    if i not in a:
        missing.append(i)
print("the missing numbers in the list are:",missing)
'''    

# 20. Write a program to perform element-wise addition of two lists.
'''
a=[1,2,3]
b=[4,5,6]
c=[]
for i in range(3):
    c.append(a[i]+b[i])
print(c)
'''

# 21. Write a Python program to find the longest increasing subsequence in a list.

'''
a = [7, 23, 15, 42, 9, 31, 18, 27, 36]

temp = [a[0]]
subsequence = []

for i in range(1, len(a)):
    if a[i] > a[i-1]:
        temp.append(a[i])
    else:
        if len(temp) > len(subsequence):
            subsequence = temp
        temp = [a[i]]

# check last subsequence
if len(temp) > len(subsequence):
    subsequence = temp

print("Longest continuous increasing subarray:", subsequence)
'''    
        
        

# 22. Write a program to group elements based on frequency.
'''
a=[10,20,10,20,3]
temp=[]
for i in a:
    if [i,a.count(i)] not in temp:
        temp.append([i,a.count(i)])
print(temp)
'''       
