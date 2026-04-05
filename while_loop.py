# PART 1 - BASIC LEVEL

# 1. PRINT NO'S FROM 1 TO 10
'''
i=1
while i < 11:
    print(i,end=" ")
    i+=1
'''

# 2. even no's from 1 to 20
'''
i=1
while i<21:
    if i %2==0:
        print(i,end=" ")
    i+=1
'''

# 3. odd no's from 1 to 20
'''
i=1
while i<21:
    if i %2!=0:
        print(i,end=" ")
    i+=1
'''

# 4. from 10 to 1 (reverse)
'''
i = 10
while i>0:
    print(i,end=" ")
    i-=1
'''

# 5. table of 5
'''
i=1
while i <11:
    print("5 *",i,"=", 5 * i)
    i+=1
'''

# PART 2 - INTERMEDIATE LEVEL

# 6. find the sum of first 10 natural numbers
'''
i=1
sum=0
while i < 11:
    sum+=i
    i+=1
print(sum)
'''

# 7. factorial
'''
f = int(input("enter a no.: "))
fact=1
while f>0:
    fact*=f
    f-=1
print("the factorial is",fact)
'''

# 8. count no. of digits in a given no.
'''
num = int(input("enter a number: "))
count=0
while num >0:
    num//=10
    count+=1
print("No. of digits",count)
'''

# 9. reverse a no.
'''
num = int(input("enter a number: "))
rev=0
while num > 0:
    x=num%10
    rev=rev*10+x
    num//=10
print("the reverse is",rev)
'''

# 10. palindrome or not
'''
num = int(input("enter a number: "))
temp = num
rev=0
while num > 0:
    x=num%10
    rev=rev*10+x
    num//=10
if temp == rev:
    print("palindrome")
else:
    print("not palindrome")
'''

# PART 3 - PATTERN BASED

#11
'''
i=1
while i <= 5:
    print("*" * i)
    i+=1
'''

#12
'''
i=1
while i < 6:
    j=1
    while j <= i:
        print(j,end="")
        j += 1
    print()
    i+=1
'''

# PART 4 - LOGICAL / REAL SCENARIO


# 13. ask user to enter password until correct password is entered.
'''
password = "JAI SRI RAM"
confirm = input("enter password: ")
while confirm != password:
    print("incorrect password. please try again")
    confirm = input("enter password: ")
print("correct password")
'''

# 14. number guessing game
'''
import random
a=random.randint(1,10)
ans=int(input("enter a no. from 1 to 10: "))
while ans != a:
    print("incorrect guess, please try again")
    ans=int(input("enter a no. from 1 to 10: "))
print("correct guess")
'''

# 15. keep taking input numbers until user enters 0, then print total sum.
'''
num = int(input("enter a no.: "))
total=0
while num != 0:
    total += num
    num = int(input("enter a no.: "))
print("the total sum is",total)
'''

# BONUS CHALLENGE ( INTERVIEW LEVEL )

# 16. fibonacci series
'''
a = 0
b = 1
n = int(input("how many terms do you want in fibonacci series: "))
if n == 1:
    print(a)
if n==2:
    print(a)
    print(b)
if n>2:
    print(a)
    print(b)
    while n>2:
        c=a+b 
        print(c)
        a=b
        b=c
        n-=1
'''

# 17. armstrong number
'''
num = int(input("enter a whole number: "))
num2=num
temp=num
final=0
total=0
count=0
if num == 0:
    count = 1
else:
    while num>0:
        num//=10
        count+=1
print("the no. of digits is",count)
while temp>0:
    final=temp%10
    total+=final**count
    temp//=10
if num2 == total:
    print(num2,"is an armstrong number.")
else:
    print(num2,"is not an armstrong number.")
'''

# 18. prime numbers from 1 to 50
'''
i = 2
print("the prime numbers from 1 to 50 are")

while i <= 50:
    j = 2
    is_prime = True
    
    while j <= int(i**0.5):
        if i % j == 0:
            is_prime = False
            break
        j += 1
    
    if is_prime:
        print(i, end=" ")
    
    i += 1
'''   
    
    


    
    

















