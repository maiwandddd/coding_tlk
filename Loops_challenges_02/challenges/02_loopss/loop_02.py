#-----------------------------------------------------------------------------
# Name:        Maiwand Alkozai
# Purpose:     to guess the right number
#
# Author:      Maiwand Alkozai
# Created:     18-Mar-2025
# Updated:     19-Mar-2025
#-----------------------------------------------------------------------------
import random

random_number = random.randint(1, 10)
myNumber = int(input("Guess the number from 1 to 10: "))

if myNumber == random_number:
    print("You win!")
else:
    print(f"Try again, the correct number was {random_number}.")

print(f"The random number is: {random_number}") .