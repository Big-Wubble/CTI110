#Hunter M.
#6/28/24
#P3HW2
#Assignment assess student understanding of decision structures


name_list = []
overtime_list = []
hours_list = []
gross_list = []

name = input("Enter employee's name: ")
while True:
    
    hours = float(input('Enter number of hours worked: '))
    pay_rate = float(input("Enter employee's pay rate: "))

    over_time = hours - 40
    over_rate = pay_rate * 1.5
    over_pay = over_time * over_rate
    reg_pay = hours * pay_rate
    max_pay = 40 * pay_rate
    gross = max_pay + over_pay
    reg_hours = hours - over_time

    name_list.append(name)
    
    if (hours > 40):
        overtime_list.append(over_time)

    if (hours > 40):
        hours_list.append(max_pay)
    else:
        hours_list.append(reg_pay)
        
    if (hours > 40):    
        gross_list.append(gross)
    else:
        gross_list.append(reg_pay)

    print('--------------------------------------------------')
    print('Employee name:   (name)')
    print('')
    print('Hours Worked    Pay Rate    Overtime    Overtime Pay    RegHour Pay   Gross Pay')
    print('----------------------------------------------------------------------------------------')

    print(hours, '          $', end='')
    print(pay_rate, '       ', end='')

    if (hours > 40):
        print (f'{over_time:.2f}', '       $', end='')
    else:
        print(0, '    $', end='')

    if (hours > 40):
        print (f'{over_pay:.2f}', '        $', end='')
    else:
        print(0, '        $', end='')

    if (hours <= 40):
        print (f'{reg_pay:.2f}', '      $', end='')
    else:
        print(f'{max_pay:.2f}', '      $', end='')


    if (hours <= 40):
        print (f'{reg_pay:.2f}')
    else:
        print(f'{gross:.2f}')

    print('')
    print('')

    again = input('Enter employees name or "Done" to terminate: ')
    if 'Done' in again:
            print(f'Total number of employees entered: ${len(name_list)}')
            print(f'Total ammount paid for overtime: ${sum(overtime_list)}')
            print(f'Total ammount paid for regular hours: ${sum(hours_list)}')
            print(f'Total ammount paid in gross: ${sum(gross_list)}')
            break
        
    else:
            name = again
            continue





















