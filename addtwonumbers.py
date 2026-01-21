a=int(input("enter the first number"))
b=int(input("enter the second number"))
c=a+b
print(f"the sum of two numbers is {c}")
#another manner
def add_two_numbers(x,y):
    return x+y
num1=int(input("enter the first number"))
num2=int(input("enter the second number"))
result=add_two_numbers(num1,num2)
print(f"the sum of two numbers is {result}")
#another manner
sum=lambda x,y:x+y
num1=int(input("enter the first number"))
num2=int(input("enter the second number"))
result=sum(num1,num2)
print(f"The sum of two numbers is {result}")
#another manner
import operator
num1=int(input("enter the first number"))
num2=int(input("enter the second number"))
result=operator.add(num1,num2)
print(f"The sum of two numbers is {result}")
#another manner
print(sum([10,5]))
#another manner
n=[int(x) for x in input("enter two numbers separated by space: ").split()]
print(f"The sum of two numbers is {sum(n)}")
#another manner
from functools import reduce
n=[int(x) for x in input("enter the two numbers separated by space:").split()]
result=list(reduce(lambda x,y:x+y,n))
print(f"The sum of two numbers is {sum(result)}")
#another manner
import numpy as py
n=[int(x) for x in input("Enter the two numbers seperated by space:").split()]
result=py.sum(n)
print(f"The sum of two numbers is {result}")
#another manner
import pandas as pd
n=[int(x) for x in input("Enter two numbers seperated by space:").split()]
result=pd.Series(n).sum()
print(f"The sum of two numbers is {result}")
#another manner
import math
n=[int(x) for x in input("Enter the two numbers seperated by space :").split()]
result=math.fsum(n)
print(f"The sum of two numbers is {result}")
#another manner
from statistics import fsum
n=[int(x) for x in input("Enter the two numbers seperated by space:").split()]
result=fsum(n)
print(f"The sum of two numbers is {result}")
