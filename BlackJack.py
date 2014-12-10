#http://www.codeskulptor.org/#user31_joOL1iMn5qi5VhI.py


# Mini-project #6 - Blackjack
# By MrL

import simplegui
import random

# load card sprite - 949x392 - source: jfitz.com
CARD_SIZE = (73, 98)
CARD_CENTER = (36.5, 49)
card_images = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/cards.jfitz.png")

CARD_BACK_SIZE = (71, 96)
CARD_BACK_CENTER = (35.5, 48)
card_back = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/card_back.png")    

# initialize some useful global variables
in_play = False
outcome = ""
score = 0

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}


# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
        
# define hand class
class Hand:
    def __init__(self):
        self.hand_cards=[]
        
    def __str__(self):
        str1='Hand contains '
        str2=''
        for i in range(len(self.hand_cards)):
            str2+=str(self.hand_cards[i].suit)+str(self.hand_cards[i].rank)+' '
        return str1+str2
    
    def add_card(self,card):
        global deck_cards
        print "Card added to hand"
        global now_card
        now_card=random.choice(deck_cards)
        self.hand_cards.append(now_card)
        
    def get_value(self):
        hand_value=0
        print 'one'
        # compute the value of the hand, see Blackjack video
        for i in range(len(self.hand_cards)):
            hand_value+=VALUES[self.hand_cards[i].rank]
            print VALUES[self.hand_cards[i].rank]
        for i in range(len(self.hand_cards)):
            if( self.hand_cards[i].rank != 'A'):
                print 'not a'
                return int(hand_value)
            else:
                if ((hand_value+10)<=21):
                    print 'a with less value'
                    return int(hand_value+10)
                else:
                    print 'a with more value'
                    return int(hand_value)
   
    def draw(self, canvas, pos):
        global now_card
        Card.draw(now_card,canvas,pos)
     
# define deck class 
class Deck:
    def __init__(self):
        global deck_cards
        deck_cards=[]
        for i in range(52):
            deck_cards.append(Card(random.choice(SUITS),random.choice(RANKS)))
        
    def __str__(self):
        global deck_cards
        str1='deck contains '
        str2=''
        for i in range(52):
            str2+=str(deck_cards[i].suit)+str(deck_cards[i].rank)+' '
        return str1+str2
    
    def deal_card(self):
        global deck_cards
        dealcard=random.choice(deck_cards)
        deck_cards.remove(dealcard)
        print "Deal Card"
        return dealcard
    
    def shuffle(self):
        global deck_cards
        random.shuffle(deck_cards)

#define event handlers for buttons
def deal():
    global message, message2,in_play,deck_cards,player,dealer,d1,score
    message='HIT or STAND?'
    message2=''
    print ''
    print "New Deal"
    if (in_play==True):
        message='You Resigned'
        message2='You Lose!?!'
        score-=1
        in_play=False
    d1=Deck()
    d1.shuffle()
    player=Hand()
    dealer=Hand()
    player.add_card(d1.deal_card)
    player.add_card(d1.deal_card)
    dealer.add_card(d1.deal_card)
    dealer.add_card(d1.deal_card)
    in_play = True

def hit():
    global player,in_play,d1,message,message2,score
    if (player.get_value()<=21 and in_play==True):
        player.add_card(d1.deal_card)
        #player added a card 
        print 'player value'+str(player.get_value())
    if (player.get_value()>21 and in_play==True):
        print "You are Busted"
        message='New Deal?'
        message2='You are Busted and Lose'
        print 'player value'+str(player.get_value())
        score-=1
        in_play=False
    
def stand():
    global message,message2,dealer,player,d1,in_play,score
    # replace with your code below
    pl=player.get_value()
    dl=dealer.get_value()
    print pl,dl
    if (in_play==False):
        print "You are Busted"
    else:
        while dealer.get_value()<=17:
            dealer.add_card(d1.deal_card)
    # if hand is in play, repeatedly hit dealer until his 
    #hand has value 17 or more
        if (int(player.get_value())<=int(dealer.get_value())):
            score-=1
            print 'Player loses'
            message2='You Lose...'
            message="New Deal?"
            in_play=False
        elif (int(player.get_value())>int(dealer.get_value())):
            score+=1
            print 'Player Wins...New Deal?'
            message2='You WIN'
            message='New Deal?'
            in_play=False
    # assign a message to outcome, update in_play and score
        

# draw handler    
def draw(canvas):
    global player,dealer
    # test to make sure that card.draw works, replace with your code below
    canvas.draw_text("BlacK JacK",[100,100],40,"Navy")
    canvas.draw_text("SCORE  "+str(score),[350,100],25,"Black")
    canvas.draw_text("Dealer",[100,200],25,"black")
    canvas.draw_text("Player",[100,400],25,"black")
    canvas.draw_text(message,[350,400],25,"Black")
    canvas.draw_text(message2,[350,200],25,"Black")
    card = Card("S", "A")
    if (in_play==True):
        canvas.draw_image(card_back,CARD_BACK_CENTER,CARD_BACK_SIZE,[130,300], CARD_SIZE)
    else:
        dealer.hand_cards[0].draw(canvas,[100,250])
    for  i in range(len(player.hand_cards)):
        player.hand_cards[i].draw(canvas,[100+80*i,450])
    for i in range(len(dealer.hand_cards)-1):
        dealer.hand_cards[i+1].draw(canvas,[100+80*(i+1),250])
        
# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_label("")
frame.add_button("Hit",  hit, 200)
frame.add_label("")
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)
frame.add_label("If the players value of the hand is less than or equal to 21, HIT adds a card to player's hand.")
frame.add_label('If the players value exceeds 21 after HIT we compare value with dealers value. Player with greater Value wins')
frame.add_label('STAND button reveals the result ')
# get things rolling
deal()
frame.start()

# remember to review the gradic rubric
