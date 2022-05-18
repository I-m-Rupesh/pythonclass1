import random as rd

print('Welcome to evodd')
choice = input('Select even or odd')
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
    print('You won!!!')
else:
    print('Bot won!!!')