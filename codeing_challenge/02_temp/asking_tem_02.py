#-----------------------------------------------------------------------------
# Name:        Maiwand Alkozai
# Purpose:     To know how cold or hot is outside
#
# Author:      Maiwand Alkozai
# Created:     19-Feb-2025
# Updated:     1-Mar-2025
#-----------------------------------------------------------------------------
myTempreture = int(input("whats the temp: "))
if 1 <= myTempreture <= 9:
    print("its so cold, stay home!")
if 10 <= myTempreture <= 20:
    print("its a nice day, you can wear a short sleeves or a t-shirt!")
if 20 <= myTempreture <= 30:
    print('its so hot outside, stay away from the sun and stay cold')