#-----------------------------------------------------------------------------
# Name:        Maiwand Alkozai
# Purpose:     To multiply and put even numbers
#
# Author:      Maiwand Alkozai
# Created:     24-Mar-2025
# Updated:     25-Mar-2025
#-----------------------------------------------------------------------------
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = [n for n in numbers if n % 2 == 0]
squared_numbers = [n ** 2 for n in even_numbers]
print(even_numbers, squared_numbers)


