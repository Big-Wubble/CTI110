# Hunter M.
# 6/20/24
# P2LAB1
# Tests knowledge of writting code that performs math calculations and displays information to users.
import math
print ('What is the radius of the circle?', end=' ')

radius = float(input())
diameter = 2*radius
circumference = 2*math.pi*radius
area = math.pi*radius**2

print ('The diameter of the circle is ', end=' ')
print(f'{diameter:.1f}')
print ('The circumference of the circle is ', end=' ')
print(f'{circumference:.2f}')
print ('The area of the circle is ', end=' ')
print(f'{area:.3f}')
