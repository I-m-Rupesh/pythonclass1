# Rock Paper Scissor
import random
option = ['rock', 'paper', 'scissor']
game = True
pscore = 0
bscore = 0
while(game):
    print('New game')
    print('Your Turn')
    player = input("Enter your choice ")
    print('Player selected', player)

    print('Computers Turn')
    bot = random.choice(option)
    print('Bot selected', bot)

    if player == bot:
        print('Tie')
    elif player == 'rock' and bot == 'scissor'  or player == 'paper' and bot == 'rock' or player == 'scissor' and bot == 'paper':
        pscore += 1
        print('Player Wins this round')
    else:
        print('Computer Wins this round')
        bscore += 1
    
    ch = int(input("Enter '1' to continue "))

    if ch != 1:
        game = False

if pscore == bscore:
    print("Game Tie")
elif pscore > bscore:
    print("Player win")
else:
    print("Computer Win")
print("Game ends")





