import random
def game(playername):
    choices=['rock','paper','scissor']
    playerchoice=input(playername+' choose rock,paper,scissor')
     if playerchoice not in choices:
        print("Invalid choice! Please choose rock, paper, or scissors.")
         return
    computerchoice=random.choice(choices)
    print('computer choice is '+computerchoice)
    if playerchoice==computerchoice:
        print('its a tie')
    elif ((playerchoice=='rock')and(computerchoice=='scissor'))or ((playerchoice=='paper')and(computerchoice=='rock'))or((playerchoice=='scissor')and(computerchoice=='paper')):
        print('the player wins')
    else:
        print('computer wins')
playername=input('enter the name of player who wants to play now')
game(playername)
