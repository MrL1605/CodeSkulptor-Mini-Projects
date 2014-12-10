#http://www.codeskulptor.org/#user30_toQyswvNOH0mi6O.py


#Memory Game
#Mini Project 5

# Importing modules
import simplegui
import random

# helper function to initialize globals
def new_game():
    global list1,state,win,turn
    list1= range(8)+range(8)
    random.shuffle(list1)
#    to see answer UNcomment the following statement
#    print list1
    state=0
    turn=0
    win=[]
    
# define event handlers
def mouseclick(pos):
    # add game state logic here
    global chances,state,list1,x1,x2,win,turn
    a=[30,60,90,120,150,180,210,240,270,300,330,360,390,420,450,480]
    label.set_text("Turns = "+str(turn))
    for x in a:
        if (pos[0]>x and pos[0]<x+30 and pos[1]>=10 and pos[1]<=80):
            if (state==0):
                state=1
                x1=x
            elif (state==1 and (x!=x1) and len(win)!=16):
                state=2
                x2=x
                turn+=1
                label.set_text("Turns = "+str(turn))
            elif ((state==3) and (x!=x1) and (x!=x2)and len(win)!=16):
                x2=x
                state=2
                turn+=1
                label.set_text("Turns = "+str(turn))
            elif (state==2 and (x!=x1) and (x!=x2)):
                if (list1[x1/30-1]==list1[x2/30-1]):
                    state=3
                    win.append(x1)
                    win.append(x2)
                    x1=x
                else:
                    state=1
                    x1=x
                    x2=0
                            
    
# cards are logically 50x100 pixels in size    
def draw(canvas):
    global list1,state,x1,x2,win,turn
    a=[30,60,90,120,150,180,210,240,270,300,330,360,390,420,450,480]
    for x in a:
        canvas.draw_polygon(([x,10],[x+30,10],[x+30,80],[x,80]),1,"white","green")
        if (state==1):
            canvas.draw_polygon(([x1,10],[x1+30,10],[x1+30,80],[x1,80]),1,"white","teal")
            canvas.draw_text(str(list1[(x1/30)-1]),[x1+5,55],40,"White")
        elif (state==2):
            canvas.draw_polygon(([x2,10],[x2+30,10],[x2+30,80],[x2,80]),1,"white","teal")
            canvas.draw_text(str(list1[(x2/30)-1]),[x2+5,55],40,"White")
            canvas.draw_polygon(([x1,10],[x1+30,10],[x1+30,80],[x1,80]),1,"white","teal")
            canvas.draw_text(str(list1[(x1/30)-1]),[x1+5,55],40,"White")
        elif (state==3):
            canvas.draw_polygon(([x1,10],[x1+30,10],[x1+30,80],[x1,80]),1,"white","teal")
            canvas.draw_text(str(list1[(x1/30)-1]),[x1+5,55],40,"White")            
        for z in win:
            canvas.draw_polygon(([z,10],[z+30,10],[z+30,80],[z,80]),1,"white","teal")
            canvas.draw_text(str(list1[(z/30)-1]),[z+5,55],40,"White")
    if (len(win)==16):
        canvas.draw_text("Finally you won at "+str(turn),[530,50],25,"Blue")
     
# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()
# Always remember to review the grading rubric
