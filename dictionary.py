# Basic 
# 1. Create a dictionary and print all keys and values.
'''
my_dict = {}

n = int(input("Enter number of elements to enter in dict.: "))

for i in range(n):
    key = input(f"Enter key {i+1}: ")
    value = input(f"Enter value {i+1}: ")
    my_dict[key] = value
print(my_dict)
'''

# 2. Count frequency of each word in a sentence.
'''
sentence = "i want to become a devotee of god sri ram"

freq = {}

for word in sentence.split():
    if word in freq:
        freq[word] += 1
    else:
        freq[word] = 1

for word, count in freq.items():
    print(f"{word}: {count}")
'''
    
# 3. Merge two dictionaries.
'''
dict1 = {
    "name": "Prashant",
    "age": 20
}

dict2 = {
    "course": "B.Tech",
    "city": "Noida"
}
dict1.update(dict2)
print(dict1)
'''

# 4. Find the length of a dictionary.
'''
dict1 = {
    "name": "Prashant",
    "age": 20
}
print("the length of the dictionary is",len(dict1))
'''

# 5. Check if a key exists in a dictionary.
'''
dict1 = {
    "name": "Prashant",
    "age": 20
}
k=input("enter the key to check: ")
for i in dict1:
    if i == k:
        print("the key exists")
        break
else:
    print("the key does not exist")
'''

# Intermediate

# 6. Sort a dictionary by values.
'''
d={"a":10,"b":20,"c":15}
x=dict(sorted(d.items(),key=lambda y: y[1]))
print(x)
'''

# 7. Find the key with the maximum value.
'''
def max_key():
    d={"a":10,"b":20}
    max_k = None
    max_v = float('-inf')
    
    for k, v in d.items():
        if v > max_v:
            max_v = v
            max_k = k
            
    return max_k
print(max_key())
'''
    
# 8. Remove a key from a dictionary.
'''
data = {'a': 10, 'b': 20, 'c': 30}
removed = data.pop('b')
print(data)      
print(removed)   
'''

# 9. Convert two lists into a dictionary.
'''
l1=['a','b']
l2=[56,78]
d={}
for i in range(len(l1)):
    d[l1[i]]=l2[i]
print(d)
'''

# 10. Count character frequency using a dictionary.
'''
def char_freq(s):
    d={}
    for i in s:
        if i in d:
            d[i]+=1
        else:
            d[i]=1
    return d
s=input("enter a string: ")
print(char_freq(s))
'''    

# Tricky 
# 11. Invert a dictionary (swap keys and values).
'''
d={"noida":5,"odisha":6}
a={}
for i,j in d.items():
    a[j]=i
print(a)
'''

# 12. Group elements by frequency using a dictionary.
'''
x=[10,20,20,30,30,30,40,40]
d={}

for i in x:
    d[i]=x.count(i)

group={}
for i,j in d.items():
    if j not in group:
        group[j]=[]
    group[j].append(i)
print(group)
'''   


# 13. Find duplicate values in a dictionary.
'''
d={"noida":5,"odisha":6,"india":5}
temp=[]
dup=[]
for i,j in d.items():
    temp.append(j)
    if temp.count(j)>1:
        if j not in dup:
            dup.append(j)
print(dup)
'''

# 14. Create a nested dictionary for student records.
'''
num = int(input("no. of students: "))
d = {}

for i in range(num):
    n = input(f"enter name{i+1}: ")
    a = int(input(f"enter age{i+1}: "))
    d[n] = {"age": a}

print(d)
'''

# 15. Flatten a nested dictionary.
'''
nested_dict = {
    'ram': {'age': 12},
    'laxman': {'age': 11},
    'hanuman': {'age': 10}
}

flat_dict = {}

for outer_key, inner_dict in nested_dict.items():
    for inner_key, value in inner_dict.items():
        flat_dict[f"{outer_key}_{inner_key}"] = value

print(flat_dict)
'''

# Mixed (String + Set + Dictionary)

# 1. Count unique words in a sentence.
'''
s = input().split()
print(sum(1 for w in set(s) if s.count(w) == 1))
'''
    
# 2. Find common characters between two strings.
'''
a=input("enter a word: ")
b=input("enter a word: ")
c=[]
for i in a:
    if i in b:
        if i not in c:
            c.append(i)
print(c)
'''

# 3. Find the most frequent character in a string.
'''
a=input("enter a word: ")
m=0
x=0
d={}
for i in a:
    d[i]=a.count(i)
for i,j in d.items():
    if m <j:
        m=j
        x=i
print("most frequent character:",x)
'''

# 4. Remove duplicate words from a sentence.
'''
sentence = input("enter a sentence: ").split()

seen = set()
result = []

for word in sentence:
    if word not in seen:
        seen.add(word)
        result.append(word)
print(" ".join(result))
'''

# 5. Find words with the same letters (anagram groups).
'''
sentence = input("enter a sentence: ").split()

groups = {}

for word in sentence:
    key = "".join(sorted(word)) 
    
    if key not in groups:
        groups[key] = []
    
    groups[key].append(word)
print(groups)
print(list(groups.values()))
'''            
