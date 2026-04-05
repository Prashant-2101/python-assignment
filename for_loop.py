# PART 1 - BASIC FOR LOOP QUESTIONS


# USE A FOR LOOP TO PRINT NUMBERS FROM 1 TO 10
"""
for i in range(1,11):
    print(i,end=' ')
"""

# PRINT EVEN NUMBERS
'''
for i in range(1,20):
    if i%2==0:
        print(i,end=' ')
'''

#FIND SUM
'''
sum=0
for i in range(1,11):
    sum+=i
print(sum)
'''

#MULTIPLICATION TABLE
'''
num = int(input("enter a number: "))
for i in range(1,11):
    print(num," * ",i," = ",num*i)
'''

#count characters
'''
word=input("enter a word: ")
count=0
for i in word:
    count+=1
print("the no. of characters are",count)
'''


# PART 2 - BREAK RELATED QUESTIONS


# stop at 5
'''
for i in range(1,10):
    if i == 5:
        break
    print(i)
'''

# search in list
'''
for i in range(20,26):
    if i == 25:
        print("found")
        break
'''

# first negative number
'''
z = [1,2,5,-10,20,-30]
for i in z:
    if i<0:
        print(i)
        break
'''


# PART 3 - CONTINUE RELATED QUESTIONS


#SKIP 5
'''
for i in range(1,11):
    if i ==5:
        continue
    print(i,end=' ')
'''

# skip even numbers
'''
for i in range(1,21):
    if i % 2 == 0:
        continue
    print(i,end=' ')
'''

# skip letter
'''
x = "python"
for i in x:
    if i=="o":
        continue
    print(i,end='')
'''


# PART 4 - PASS RELATED QUESTIONS


# empty loop
'''
for i in range(1,5):
    pass
'''

# skip using pass
'''
for i in range(1,10):
    if i == 6:
        pass
'''


# PART 5 - FOR-ELSE QUESTIONS


# search number using for-else
'''
a = [25,50,75,100]
for i in a:
    if i == 100:
        print("Found")
        break
else:
    print("Not Found")
'''

# prime number check
'''
num = int(input("enter a number: "))
for i in range(2,(int(num**0.5))+1):
    if num % i == 0:
        print("not prime")
        break
else:
    print("prime")
'''


# PART 6 - PATTERN QUESTIONS


# star pattern
'''
for i in range(1,6):
    for j in range(1,i+1):
        print("*",end="")
    print()
'''

# reverse star pattern
'''
k=7
for i in range(1,6):
    k-=1
    for j in range(1,k):
        print("*",end="")
    print()
'''

# number pattern
'''
for i in range(1,6):
    for j in range(1,i+1):
        print(j,end="")
    print()
'''

# same number pattern
'''
for i in range(1,6):
    for j in range(1,i+1):
        print(i,end="")
    print()
'''

# pyramid pattern
'''
for i in range(1,6):
    for j in range(1,6-i):
        print(" ",end ="")
    for k in range(2*i-1):
        print("*",end="")
    print()
'''

# inverted pyramid
'''
for i in range(5,0,-1):
    for j in range(1,6-i):
        print(" ",end ="")
    for k in range(2*i-1):
        print("*",end="")
    print()
'''    

# break in pattern (BONUS QUESTION)
'''
for i in range(1,6):
    if i == 4:
        break
    for j in range(1,6):
        print("*",end="")
    print()
'''
