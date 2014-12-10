#http://www.codeskulptor.org/#user30_YW5OMEPQEnl45TL.py

#Screen Saver Upgraded
#import modules
import simplegui

#define global variables
message="Welcome!"
position =[0,32]
flag =[0,0]
color="White"

#define time handlers
def slider():
     global position, flag
     if (flag[0]==0):
           position[0]+=1
     elif (flag[0]==1):
           position[0]-=1
     if (flag[1]==0):
           position[1]+=1
     elif (flag[1]==1):
           position[1]-=1
     if(position[0]>=255):
           flag[0]=1
     elif(position[0]<=0):
           flag[0]=0
     if(position[1]>=270):
           flag[1]=1
     elif(position[1]<=32):
           flag[1]=0

#define input handlers                                                           
def input_color(strn):
      global color
      color=strn
 
def input_field(strn):
     global message,position_max 
     message =strn

#define input handler
def display(canvas):
     canvas.draw_text(message, position,35,color)

#create frame
frame=simplegui.create_frame("Screen Saver",400,300)

#create handlers
screen=frame.set_draw_handler(display)
text=frame.add_input("Message",input_field,100)
text2=frame.add_input("Color",input_color,100)
timer=simplegui.create_timer(20, slider)

#start timer and frame
frame.start()
timer.start()
