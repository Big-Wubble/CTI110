#hunter M.
#7/4/2024
#P4LAB2
#Assignment tests student's knowledge of how to write code that displays information to users using loops.


end = 1
num = 0  
while True:
    num = int(input('Enter an integer: '))

    for i in range(0,13):
     if num >= 0:
        print(f' {num} * {i} = {num*i}')
        end = end+1
    if end == 14:
        again = input('would you like to run program again? (y/n): ')
        if 'y' in again:
            num = 0
            end = 1
            continue
        elif 'n' in again:
            print("Good Bye")
            break
        else:
            print("Invalid Input")
