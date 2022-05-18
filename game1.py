import random as rd

print('Welcome to evodd')

game = True

while game:

    choice = input('Select even or odd\n')
    mynum = int(input("My turn "))
    print('bot turn')
    botnum = rd.randint(1,10)
    print('Bot selected ', botnum)
    add = mynum + botnum

    rem =  add % 2
    if rem == 0:
        ans = 'even'
    else:
        ans = 'odd'

    if choice == ans:
        print('You won!!!\n\n')
    else:
        print('Bot won!!!\n\n')

    ch=int(input('Press "1" to continue !!'))
    
    if ch != 1:
        game = False
        print("Thank you!")
    