
import random as rd

print('Welcome to evodd')

game = True
uscore = 0
bscore = 0
while game:
    choice = input('Select even or odd\n')
    mynum = int(input("My turn "))
    print('\n\nbot turn')
    botnum = rd.randint(1,10)
    print('Bot selected ', botnum)
    add = mynum + botnum

    rem =  add % 2
    if rem == 0:
        ans = 'even'
    else:
        ans = 'odd'

    if choice == ans:
        uscore += 1
        print('You won!!!\n\n')
    else:
        bscore += 1
        print('Bot won!!!\n\n')

    ch = int(input('Enter "1" to continue !!'))
    if ch != 1:
        game = False
        if uscore > bscore:
            print("Player Won the game")
        elif uscore < bscore:
            print("Bot Won the game")
        else:
            print("Game Draw")
        print("Thank you for playing!!")
    