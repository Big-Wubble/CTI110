#Hunter M.
#6/15/24
#P1HW2
#Learning how to create a program that does some basic math on numbers that are entered.

print('This program calculates and displays travel expenses')
print(' ')
print('Enter Budget: ', end='')
budget = int(input())
print(' ')
print('Enter your travel destination: ', end='')
location = input()
print(' ')
print('How much do you think you will spend on gas?: ', end='')
fuel = int(input())
print(' ')
print('Approximately, how much will you need for accomidation/hotel?: ', end='')
accomidation = int(input())
print(' ')
print('Last, how much do you need for food?: ', end='')
food = int(input())

print(' ')
print(' ')

print('------------Travel Expenses------------')
print(f'Location:            {location}')
print(f'Initial Budget:      ${budget}')
print(f'Fuel:                ${fuel}')
print(f'Accomidation:        ${accomidation}')
print(f'Food:                ${food}')
print('---------------------------------------')
print(' ')
print(f'Remaining Ballance:  ${budget-fuel-accomidation-food}')
