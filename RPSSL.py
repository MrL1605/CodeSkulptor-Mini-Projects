#http://www.codeskulptor.org/#user29_eVoY8ukvLY0kk73.py
"""0 - rock,1 - Spock,2 - paper,3 - lizard,4 - scissors"""
import random
def name_to_number(name):
    #converts name to number
   
    if (name=='rock'):
        return 0
    elif (name=='spock'):
        return 1
    elif (name=='paper'):
        return 2
    elif (name=='lizard'):
        return 3
    elif (name=='scissors'):
        return 4
#
def number_to_name(number):
    #converts number to name
    if (number==0):
        return 'rock'
    elif (number==1):
        return 'spock'
    elif (number==2):
        return 'paper'
    elif (number==3):
        return 'lizard'
    elif (number==4):
        return 'scissors'
#    
def rpsls(player_choice): 
    # randomly chooses computer guess 
    # and returns the winnner
    
    player_number=name_to_number(player_choice)
    guess=random.choice([0,1,2,3,4])
    result=(player_number-guess)%5
    print''
    print "Player's choice is "+player_choice
    
    #or guess=random.randrange(0,5)
    
    print "Computer's choice is "+number_to_name(guess)
    if (guess == player_number):
        print 'Player and Computer tie'
    elif (result==1 or result==2):
        print 'Player won'
    elif (result==3 or result==4):
        print 'Computer won'

#INputs
rpsls("rock")
rpsls("spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")
#END



