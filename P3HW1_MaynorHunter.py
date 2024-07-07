#Hunter M.
#6/28/24
#P3HW1
# This program takes a number grade , determines average and displays letter grade for average.

# Enter grades for six modules
mod_1 = float(input('Enter grade for Module 1: '))
mod_2 = float(input('Enter grade for Module 2: '))
mod_3 = float(input('Enter grade for Module 3: '))
mod_4 = float(input('Enter grade for Module 1: '))
mod_5 = float(input('Enter grade for Module 5: '))
mod_6 = float(input('Enter grade for Module 6: '))

print (' ')
print (' ')

# add grades entered to a list
grades = [mod_1, mod_2, mod_3, mod_4, mod_5]

# TO DO: determine lowest, highest , sum and average for grades
low = min(grades)
high = max(grades)
total = sum(grades)
avg = total/len(grades)

# determine letter grade for average
print('-------------------Results------------------------')
print (f'Lowest Grade:                {low:.1f}')
print (f'Highest Grade:               {high:.1f}')
print (f'Sum of Grades:               {total:.1f}')
print (f'Average:                     {avg:.2f}')
print('--------------------------------------------------')

if (avg >= 90):
    print ('Your grade is : A')
if (avg <= 89) and (avg >= 80):
    print ('Your grade is : B')
if (avg <= 79) and (avg >= 70):
    print ('Your grade is : C')
if (avg <= 69) and (avg >= 60):
    print ('Your grade is : D')
if (avg <= 59):
    print ('Your grade is : F')





