#http://www.codeskulptor.org/#user29_QApj5HKMHHjVSDp.py

#SCREEN SAVER
#import requried modules
import simplegui
import random

#global variables
message="Welcome!"
lalit="By MrL"
position = [160,160]

#draw handlers
def display_message(canvas):
    canvas.draw_text(message,position,25,"BLue")	    
    canvas.draw_text(lalit, [350,280],15,"Red")

def time_handler():
    global position
    position[0]=random.randrange(0,350)
    position[1]=random.randrange(0,250)
                                
#draw input handlers
def modify_message(new):
    global message
    message=new
    
#create frame
frame=simplegui.create_frame("Screen Saver",400,300)

#register event handlers
screen=frame.set_draw_handler(display_message)
text=frame.add_input("Message",modify_message,180)
timer=simplegui.create_timer(2000, time_handler)
label=frame.add_label("Description:")
label2=frame.add_label("Give a name in box above to make it a Screen Saver in the box to the right")

#start frame
timer.start()
frame.start()


