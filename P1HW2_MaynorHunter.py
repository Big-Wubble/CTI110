#Hunter M.
#6/15/24
#P1HW2
#Learning how to create a program that does some basic math on numbers that are entered.

print('This program calculates and displays travel expenses')

print('Enter Budget: ', end='')
budget = int(input())

print('Enter your travel destination: ', end='')
location = input()

print('How much do you think you will spend on gas?: ', end='')
fuel = int(input())

print('Approximately, how much will you need for accomidation/hotel?: ', end='')
accomidation = int(input())

print('Last, how much do you need for food?: ', end='')
food = int(input())

print(' ')
print(' ')

print('------------Travel Expenses------------')
print('Location: ', location)
print('Initial Budget: ', budget)
print(' ')
print('Fuel: ', fuel)
print('Accomidation: ', accomidation)
print('Food: ', food)
print(' ')
print('Remaining Ballance: ', budget-fuel-accomidation-food)
