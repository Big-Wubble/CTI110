# Hunter M.
# 6/20/24
# P2LAB2
# Tests knowledge of writting code that uses a dictionary to store user input and displays output to the user.

car_dict = {'Camaro': 18.21, 'Prius': 52.36, 'Model S': 110, 'Silverado': 26}
keys = car_dict.keys()
print(keys)

name = input("Enter a vehicle to see it's mpg: ")

mpg = car_dict[name]
print(f'The {name} gets {mpg} mpg.')

miles = float(input(f'how many miles wil you drive the {name}?'))
gallons = miles/mpg
print(f'{gallons:.2f} gallons of gas are needed to drive the {name} {miles} miles.')
