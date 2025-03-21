#-----------------------------------------------------------------------------
# Name:        Maiwand Alkozai
# Purpose:     to skip the even numbers
#
# Author:      Maiwand Alkozai
# Created:     19-Mar-2025
# Updated:     20-Mar-2025
#-----------------------------------------------------------------------------
n = 10
while n > 0 and input(f"{n} Type 'stop' to quit: ").strip().lower() != "stop":
    n -= 1
print("Stopped!" if n > 0 else "Countdown completed!")
