You are tasked with writing a Python program that calculates income tax for individuals
based on their income and tax brackets. Your program should follow these rules:
The tax calculation is based on the following tax brackets:
• Up to $10,000: 5% tax
• $10,001 to $50,000: 10% tax
• $50,001 to $100,000: 20% tax
• Over $100,000: 30% tax
There is also an additional tax deduction of $500 for individuals over 65 years old. If an 
individual has children, they receive a tax credit of $200 for each child. Write a Python 
program that takes input for an individual's income, age, and the number of children 
and calculates their income tax.


X, Y, Z = map(int,input("income,age,children: ").split())
if Y>65 and Z==0:
     X = X-500
     if X<=10001:
         print("5%tax")
     elif 10001<x<=50000:
         print("10% tax")
     elif 50000<x<=100000:
         print("20% tax")
     else:
         print("30% tax")

if Z>0:
    X = X+(200*Z)
    if X<=10001:
         print("5%tax")
    elif 10001<x<=50000:
         print("10% tax")
    elif 50000<x<=100000:
         print("20% tax")
    else:
         print("30% tax")
