# Beginner Level

# 1. Lambda Basics

# o Write a lambda function to add two numbers.
'''
add = lambda a,b:a+b
print(add(10,15))
'''

# o Write a lambda function to check if a number is even or odd.
'''
even_odd=lambda n: "even" if n % 2==0 else "odd"
print(even_odd(8))
'''

# 2. Using map()

# o Given a list of integers, use map() to create a new list with each number squared.
'''
print(list(map(lambda x: x**2,[10,20,30])))
'''

# o Convert a list of strings to uppercase using map().
'''
print(list(map(lambda x: x.upper(),["jai","sri","ram"])))
'''

# 3. Using filter()

# o Given a list of numbers, filter out only even numbers.
'''
print(list(filter(lambda x: x if x%2==0 else None,[12,34,57,79,90])))
'''

# o Filter words that have length greater than 5 from a list of strings.
'''
print(list(filter(lambda x:True if len(x)>5 else False,["prashant","noida","india"])))
'''

# 4. Using reduce()  

# o Find the sum of all elements in a list using reduce().
'''
from functools import reduce
li=[10,20,30]
print(reduce(lambda x,y:x+y, li))
'''

# o Find the product of all numbers in a list.
'''
from functools import reduce
li=[10,20,30]
print(reduce(lambda x,y:x*y, li))
'''

# Intermediate Level

# 5. Combination of lambda + map  
# o Given a list of numbers, return a list where each number is multiplied by 10.
'''
a=[12,34,56,78,90]
print(list(map(lambda b: b*10,a)))
'''

# 6. Combination of lambda + filter  
# o From a list of numbers, filter out all numbers divisible by 3.
'''
a=[12,34,56,78,90]
print(list(filter(lambda b:b%3==0,a)))
'''

# 7. Using reduce() for maximum  
# o Find the maximum number in a list using reduce().
'''
from functools import reduce
c=[12,34,56,78,90]
print(reduce(lambda a,b:a if a>b else b,c ))
'''

# 8. String Manipulation  
# o Given a list of names, use map() to return names with their first letter capitalized.  
'''
print(list(map(lambda b:b.capitalize(),["sita","ram"])))
'''

# 9. Filter Palindromes  
# o Given a list of strings, filter out only palindrome words using filter().
'''
print(list(filter(lambda x: x==x[::-1],["ram","madam"])))
'''
