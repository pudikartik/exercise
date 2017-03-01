# Code to execute rock paper scissors game 
# take input from two players
a=input('Lets play rock, paper and scissors (yes/no): ')
def game(a,b):
    if (a=='rock' and b=='scissors') or (a=='scissors' and b=='paper') or (a=='paper' and b=='rock'):
        print('Player 1 wins!')
        draw=False
    elif(b=='rock' and a=='scissors') or (b=='scissors' and a=='paper') or (b=='paper' and a=='rock'):
        print('player 2 wins!')
        draw=False
    elif a==b:
        print('it is a tie. Please play again')
        draw=True
    return draw
if a =='yes':
    while a=='yes' or draw==True:
        player1=input('input first player choice: ')
        player2=input('input second player choice: ')
        sample=['rock','paper','scissors']
        if ((player1 in sample) and (player2 in sample)):
            draw=game(player1,player2)
            if draw==False:
                a=input('Do u wanna play another game (yes/no): ')
        else:
            print('Invalid Input. The player can only select (rock, paper, scissors)')
elif a =='no':
    print('thanks for playing')
else:
    print('invalid input')
