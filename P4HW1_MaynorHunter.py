#Hunter M.
#7/5/24
#P4HW1
#Assignment assess student ability to edit and enhance exiting programs

score_num = int(input("How many scores do you want to enter? "))
score_list = set([])
index = 1
while index <= score_num:
    print(f'Enter score #', index, end='')
    score = float(input(': '))
    if 0 <= score <= 100:
        score_list.add(score)
        index = index + 1
        continue
    else:
        print("Invalid score entered!!!!")
        print("Score should be between 0 and 100")

average = sum(score_list)/len(score_list)
print('-------------------Results------------------------')

print(f'Lowest Score   :  {min(score_list):.2f}')
score_list.remove(min(score_list))
print(f'Modified List  : ', score_list)
print(f'Scores Adverage:  {average}')

if average >= 90:
    print('Grade          :  A')        
elif 89 >= average >= 80:
    print('Grade          :  B') 
elif 79 >= average >= 70:
    print('Grade          :  C')
elif 69 >= average >= 60:
    print('Grade          :  D') 
else:
    print('Grade          :  F')

#print (f'Average:                     {average:.2f}')

print('--------------------------------------------------')
 
