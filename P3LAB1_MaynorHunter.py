#Hunter M.
#6/28/24
#P3LAB1
#Assignment tests student's knowledge of how to write code that displays information to users

quarter = 0.25
dime = 0.10
nickel = 0.05
penny = 0.01
base_money = float(input('Enter the amount of money as a float: $'))

dollars = base_money//1
if dollars == 1:
    print (int(dollars), 'Dollar')
if dollars > 1:
    print (int(dollars), 'Dollars')

cents = base_money - dollars

quarters = cents//quarter
if quarters == 1:
    print (int(quarters), 'Quarter')
if quarters > 1:
    print (int(quarters), 'Quarters')
if cents >= 0.25: 
    cents = cents - (quarter*quarters)

dimes = cents//dime
if dimes == 1:
    print (int(dimes), 'Dime')
if dimes > 1:
    print (int(dimes), 'Dimes')
if cents >= 0.10: 
    cents = cents - (dime*dimes)

nickels = cents//nickel
if nickels == 1:
    print (int(nickels), 'Nickel')
if nickels > 1:
    print (int(nickels), 'Nickels')
if cents >= 0.05: 
    cents = cents - (nickel*nickels)

pennies = cents//penny
if pennies == 1:
    print (int(pennies), 'Penny')
if pennies > 1:
    print (int(pennies), 'Pennies')


