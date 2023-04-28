import random as r

#starting the game - input

start = (input('do u want to start the game? (Y/N): ').lower())


#starting the game - code

if start == 'y':
    print("""// WELCOME TO ROULETTE WITH MATHS //
                    // Made by Vidha //
                  // GAME IS STARTING //""")

elif start == 'n':
    print('// GAME EXITED, THANKYOU FOR PLAYING //')
    exit()
else:
    print('// error, please enter Y/N //')

#game information

print ("""  This is the ROULETTE BOARD we'll be referring to:
            A => |   | 3 | 6 | 9 | 12 | 15 | 18 | 21 | 24 | 27 | 30 | 33 | 36 | 3rd row
            B => | 0 | 2 | 5 | 8 | 11 | 14 | 17 | 20 | 23 | 26 | 29 | 32 | 35 | 2nd row
            C => |   | 1 | 4 | 7 | 10 | 13 | 16 | 19 | 22 | 25 | 28 | 31 | 34 | 1st row
            D => ----|    1st twelve  |     2nd twelve    |     3rd twelve    |--------
            E => ----| 1-18  |  even  |         |         |   odd   |  19-36  |--------
           -----------------------------------------------------------------------------
            Points to Ponder:
                => Rows A, B, C & D make your amount thrice of the deposited amount.
                => Row E makes your amount twice of the deposited amount.
                => Choosing a single number on the board will make your deposited amount reset to zero.""")
print('---------------------------------------------------------------------------------------------------------------- \n')



print ("""SELECT THE CATEGORY TO BET ON:\n
       1. if you want to bet on even numbers, type eve \n
       2. if you want to bet on odd numbers, type odd \n
       3. if you want to bet on numbers from 1-18, type s1 \n
       4. if you want to bet on numbers from 19-36, type s2 \n
       5. if you want to bet on first set of 12 numbers, type f12 \n
       6. if you want to bet on second set of 12 numbers, type se12 \n
       7. if you want to bet on third set of 12 numbers, type t12 \n
       8. if you want to bet on 1st row, type r1 \n
       9. if you want to bet on 2nd row, type r2 \n
       10. if you want to bet on 3rd row, type r3 \n
       11. if you want to bet on 0, type 0""")
print('---------------------------------------------------------------')

row=[]
for j in range(0,37):
    row.append(j)

category = str(input('enter your category: ').lower())

#amount to be deposited

def deposit(): 
    while True:
        bal =  int(input(' now enter your bet amount: $'))
        if bal>0:
            break
        elif bal == 0:
            print('entered amount cannot be 0, please enter a valid amount.')
        else:
            print('please enter a valid amount.')
    return bal

new_amt = deposit() #dummy variable for amount + calling the amount


i = r.randint(0,38) #rolling out the pin for a random number using random module

if i%2==0 and category == 'eve':  #bet on even
    new_amt*=2
    print('you won the bet! your amount just got doubled! congratulations!')

elif i%2!=0 and category == 'odd':  #bet on odd
    new_amt*=2
    print('you won the bet! your amount just got doubled! congratulations!')

elif i in range(1,19) and category == 's1':  #bet on 1-18
    new_amt*=2
    print('you won the bet! your amount just got doubled! congratulations!')

elif i in range(19,37) and category == 's2':  #bet on 19-36
    new_amt*=2
    print('you won the bet! your amount just got doubled! congratulations!')

elif i in range(1,12) and category == 'f12':    #bet on first twelve
    new_amt*=3
    print('you won the bet! your amount just got x3! congratulations!')

elif i in range(15,23) and category == 'se12':   #bet on 2nd twelve
    new_amt*=3
    print('you won the bet! your amount just got x3! congratulations!')

elif i in range(22,37) and category == 't12':    #bet on 3rd twelve
    new_amt*=3
    print('you won the bet! your amount just got x3! congratulations!')

elif i in row:
    if j in range(3,37,3) and category == 'r3':  #bet on 3rd row
        new_amt*=3
        print('you won the bet! your amount just got x3! congratulations!')

elif i in row:
    for k in range(2,36,3) and category == 'r2':     #bet on 2nd row
        new_amt*=3
        print('you won the bet! your amount just got x3! congratulations!')

elif i in row:
    for l in range(1,35, 3) and category == 'r1':   #bet on 1st row
        new_amt*=3
        print('you won the bet! your amount just got x3! congratulations!')

elif i==0 and category == '0':  #bet on zero
    new_amt*=2
    print('you won the bet! your amount just got doubled! congratulations!')

else:
    new_amt = 0

print("you're on the amount of $",new_amt)
