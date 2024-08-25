s = input("enter a word: ")
temp = s
str = ""
for i in s:
    str = i + str
if temp == str:
    print("this is a palindrome")
else:
    print("this is not a palindrome")
