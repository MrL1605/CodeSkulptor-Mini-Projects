#http://www.codeskulptor.org/#user29_kNcTknxtigWdgMT.py
# Mini Project-3 "Guess The Number"
# Importing modules
import random
import simplegui

# global variables 
num_range=100
lalit="By MrL"

# Helper Function
def new_game():
    global num_range
    if (num_range==100):
        range100()
    elif (num_range==1000):
        range1000()

# Event Handlers
def range100():
    global num                      
    global count
    global num_range
    num_range=100
    num=random.randrange(0,100)
    count=7
    print "\nNew game.\nRange is 0 to 100" 
    print "You got 7 chances"

def range1000():
    global num
    global count
    global num_range
    num_range=1000
    num=random.randrange(0,1000)
    count=10
    print "\nNew game.\nRange is 0 to 1000"
    print "You got 10 chances"
    
def input_guess(guess):
    global count
    global num
    guess=int(guess)
    count=count-1
    print "\nNumber of chances left",count
    print "Your Guess is ",guess
    #Comparision of Guess and Number
    if (num>guess):
        print 'Higher!'
    elif (num<guess):
        print 'Lower!'
    elif (num==guess):
        print 'Correct!!!'
        print "Yooo. You found the number."
        print "Let's play another game."
        new_game()
    else:
        print "Don't know"
    #Ended number of chances
    if (count==0):
        print "Seems you couldn't find the number"
        print "Number was",num
        print "Let's play another game"
        new_game()

def display_timer(canvas):
    canvas.draw_text(lalit, [250,280], 15, "RED")
# Create Frame
frame = simplegui.create_frame("Guess",300,300)
#Control Elements
frame.add_button("Range is [0,100)", range100,200)
frame.add_button("Range is [0,1000)", range1000,200)
frame.add_input("Enter guess",input_guess,200)
screen=frame.set_draw_handler(display_timer)
frame.add_label("Description:")
frame.add_label("Look at window to the right of you where New Game is Printed.")
frame.add_label("Guess the number between the given range and find the secret number before you run out of number of chances.") 
# Call new_game and Start frame
new_game()
frame.start()


