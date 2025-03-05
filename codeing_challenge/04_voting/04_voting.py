#-----------------------------------------------------------------------------
# Name:        Maiwand Alkozai
# Purpose:     To know at what age we can vote
#
# Author:      Maiwand Alkozai
# Created:     26-Feb-2025
# Updated:     2-Mar-2025
#-----------------------------------------------------------------------------
print("hey maiwand how can i help you?")
input("")
print("well, you found your guy!")
myScore = int(input("Enter your age: "))
if 1 <= myScore <= 10:
    print("well..uh thats too young to vote")
if 10 < myScore <= 17:
    print("still underage, you cant vote")
if 18 <= myScore <= 50:
    print("yes you can vote!")

