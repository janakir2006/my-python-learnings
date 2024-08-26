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


income,age,kids = map(int,input("income,age,kids: ").split())
if age>65 and kids==0:
     if income<=10000:
         print((5/100)*income)-500)
     elif 10001<=income<=50000:
         print((10/100)*income)-500)
     elif 50001<=income<=100000:
         print((20/100)*income)-500)
     else:
         print((30/100)*income)-500)

if kids>0:
    if income<=10000:
         print((5/100)*income)-(200*kids))
    elif 10001<=income<=50000:
         print((10/100)*income)-(200*kids))
    elif 50001<=income<=100000:
         print((20/100)*income)-(200*kids))
    else:
         print((30/100)*income)-(200*kids))
