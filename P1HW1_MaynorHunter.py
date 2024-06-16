#Maynor
#6/15
#P1HW1
#writting code that collects information from user

print('-----Calculating Exponents-----')
print('Enter an integer as the base value: ', end=' ')
base = int(input())
print('Enter an integer as the expnent: ', end=' ')
expnent = int(input())

print(base, 'raised to the power of ', expnent, 'is ', base**expnent)

print('-----Addition and Subtraction-----')
print('Enter a starter integer: ', end=' ')
start = int(input())
print('Enter an integer to add: ', end=' ')
add = int(input())
print('Enter an integer to subtract: ', end=' ')
subtract = int(input())

print(start, '+', add, '-', subtract, 'is equal to ', start + add - subtract)
