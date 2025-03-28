#-----------------------------------------------------------------------------
# Name:        Maiwand Alkozai
# Purpose:     To swap the numbers between two
#
# Author:      Maiwand Alkozai
# Created:     27-Mar-2025
# Updated:     28-Mar-2025
#-----------------------------------------------------------------------------
myScore = int(input("Enter your number maiwand: "))
if myScore in (5, 10):
    swapped_values = (10, 5) if myScore == 5 else (5, 10)
    print("Swapped values:", swapped_values)