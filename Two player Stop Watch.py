#http://www.codeskulptor.org/#user30_Tc049ZdZOzX2iRs.py

#STOPWATCH  GAME
#import modules

import simplegui

#global Varibles
a=0
b=0
c=0
player1_name="Lalit"
player2_name="Sumit"
lalit="By MrL"
chances=[0,0]
total=[0,0]
#draw handlers
def display_timer(canvas):
    global a,b,c
    if (a<10):
        a='0'+str(a)
    if (b<10):
        b='0'+str(b)
    canvas.draw_text("StopWatch",[95,30],25,"White")
    canvas.draw_text(player1_name+' '+str(chances[0])+'/'+str(total[0]),[10,60],20,"Teal")
    canvas.draw_text(player2_name+' '+str(chances[1])+'/'+str(total[1]),[210,60],20,"Teal")
    canvas.draw_text(str(a)+':'+str(b)+'.'+str(c),[110,150],25,"Gold")
    canvas.draw_text(lalit, [250,240], 15, "RED")
    if ((total[0] and total[1])>=5):
        if (chances[0]<chances[1]):
            canvas.draw_text(player2_name+" Wins",[35,205],20,"Green")
        elif (chances[0]>chances[1]):
            canvas.draw_text(player1_name+" Wins",[35,205],20,"Green")
        elif (chances[0]==chances[1]):
            canvas.draw_text("Both seem to be Competitor",[35,205],20,"Green")
    a=int(a)
    b=int(b)
    c=int(c)
    
        
        
def time_handler(): 
    global a,b,c
    c+=1
    if (c==10):
        b+=1
        c=0
        if (b==60):
            a+=1
            b=0    

def key_down_handler(key):
    pause_timer()
    
def player1n(str):
    global player1_name
    player1_name=str

def player2n(str):
    global player2_name
    player2_name=str
    
def start_timer():
    timer.start()
     
def pause_timer():
    global chances, total
    if (c==9 or c==0 ):
        chances[0]+=3
    else:
        chances[0]-=1
    total[0]+=1

def pause_timer2():
    global chances, total
    if (c==9 or c==0 or c==8):
        chances[1]+=3
    else:
        chances[1]-=1
    total[1]+=1

def stop_timer():
    global chances
    global total
    global a,b,c
    timer.stop()
    total=[0,0] 
    chances=[0,0]
    a=0 
    b=0
    c=0
    
#create frame
frame= simplegui.create_frame("StopWatch",300,300)

#register event handlers
screen=frame.set_draw_handler(display_timer)
timer=simplegui.create_timer(100, time_handler)
player1=frame.add_input("Player 1",player1n,150)
player2=frame.add_input("Player 2",player2n,150)
button1=frame.add_button("Start",start_timer,150)
button2=frame.add_button("Stop",pause_timer2,150)
button3=frame.add_button("Reset",stop_timer,150)
key=frame.set_keydown_handler(key_down_handler)

#start frame
frame.start()

