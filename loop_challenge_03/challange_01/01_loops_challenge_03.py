#-----------------------------------------------------------------------------
# Name:        Maiwand Alkozai
# Purpose:     To change the age, and subject
#
# Author:      Maiwand Alkozai
# Created:     24-Mar-2025
# Updated:     25-Mar-2025
#-----------------------------------------------------------------------------
students = [['Alice', 25, 'Physics'], ['Bob', 22, 'Chemistry'], ['Charlie', 24, 'Biology']]
students[1] = ['Bob', 23, 'Mathematics']
print(students)
for student in students:
    if student[2] == 'Biology':
        print(student[0])
        .

