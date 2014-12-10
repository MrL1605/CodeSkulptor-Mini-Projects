#http://www.codeskulptor.org/#user29_qxIZGmgbrCKl3fB.py

# money to dollar and cents
#import requried modules
import simplegui
import random

#global variables
message="Welcome!"
lalit="By MrL"
position=[80,160]

#draw handlers
def printing(dollar_d,dollar_c):
    global message
    message="You have "
    if (dollar_d>1):
        message=message+str(dollar_d)+" dollars "
    elif (dollar_d==1):
        message=message+"a dollar "
    if (dollar_c>1):
        message=message+str(dollar_c)+" and cents."
    elif (dollar_c==1):
        message=message+"and a cent."

def modify_message(money):
    global message
    dollar=float(money)
    dollar_d=int(dollar)
    dollar_c=int(round((dollar-int(dollar))*100))
    if (dollar_d==0 and dollar_c==0):
        message="You really got nothing???"
    else :
        printing(dollar_d,dollar_c)
    
#draw input handlers

def screen(canvas):
    canvas.draw_text(message,position,20,"Blue")
    canvas.draw_text(lalit,[350,280],15,"RED")

#create frame
frame=simplegui.create_frame("Name",450,300)

#register event handlers
text=frame.add_input("Enter Your Money $",modify_message,180)
sscreen=frame.set_draw_handler(screen)
label3=frame.add_label("Description:")
label=frame.add_label("Money in terms of $XX.YY")
label2=frame.add_label("Do try 0.0 , XX.01 , 1.YY")
#start frame
frame.start()
