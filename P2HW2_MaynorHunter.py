#Hunter M.
#6/21/24
#P2HW2
#Assignment assess student understanding of Lists

module1 = float(input("Enter a grade for module1: "))
module2 = float(input("Enter a grade for module2: "))
module3 = float(input("Enter a grade for module3: "))
module4 = float(input("Enter a grade for module4: "))
module5 = float(input("Enter a grade for module5: "))
module6 = float(input("Enter a grade for module6: "))

print (' ')
print (' ')

grade_list = [module1, module2, module3, module4, module5, module6]
total = module1+module2+module3+module4+module5+module6
average = total/len(grade_list)


print('-------------------Results------------------------')

print (f'Lowest Grade:                {min(grade_list):.2f}')
print (f'Highest Grade:               {max(grade_list):.2f}')
print (f'Sum of Grades:               {total:.2f}')
print (f'Average:                     {average:.2f}')

print('--------------------------------------------------')



