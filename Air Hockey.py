#http://www.codeskulptor.org/#user30_lfTcyKK727BW8KH.py

# PONG GAME
# By  MrL

#Importing modules
import simplegui
import random

#Initialize globals variables
width = 600
height = 400       
ball_radius = 20
pad_width = 8
pad_height = 80
half_pad_width = pad_width / 2
half_pad_height = pad_height / 2
right=1
left=0
time=0
# Initialize ball_pos and ball_vel
ball_pos=[width/2,height/2]
ball_vel=[0,0]
pad1_pos=[0,height/2-pad_height/2]
pad2_pos=[width-pad_width,height/2-pad_height/2]
pad1_vel=0
pad2_vel=0
score1=0
score2=0
player1_name="Player1"
player2_name="Player2"
player1_colour="White"
player2_colour="white"
# Changing Player 1 Name
def play1(player1):
    global player1_name
    player1_name=player1
    
# Changing Player 2 Name
def play2(player2):
    global player2_name
    player2_name=player2

# Changing ball direction and position
def spawn_ball(direction):
    global ball_pos, ball_vel
    ball_pos=[width/2,height/2]
    if (direction==right):
        ball_vel=[2,2]
    elif (direction==left):
        ball_vel=[-2,2]
 
# Define Button handler
def new_game():
    global pad1_pos,pad2_pos,pad1_vel,pad2_vel
    global score1,score2
    score1=0
    score2=0
    pad1_pos=[0,height/2-pad_height/2]
    pad2_pos=[width-pad_width,height/2-pad_height/2]
    pad1_vel=0
    pad2_vel=0
    spawn_ball(right)

# Update Positon of Ball
def update_ball():
    global ball_pos,ball_vel,pad1_pos,pad2_pos,height,width,ball_radius
    global score1,score2
    ball_pos[0]+=ball_vel[0]
    ball_pos[1]+=ball_vel[1]
    # Vertical Ball Restriction
    if (ball_pos[1]<ball_radius):
        ball_pos[1]=ball_radius
        ball_vel[1]=-ball_vel[1]
    elif (ball_pos[1]>(height-ball_radius)):
        ball_pos[1]=(height-ball_radius)
        ball_vel[1]=-ball_vel[1]
    # Horizontal Ball Restriction 
    if (ball_pos[0]==(pad_width+ball_radius)):
        if (ball_pos[1]<=pad1_pos[1] or ball_pos[1]>=(pad1_pos[1]+80)):
            score2+=1
            spawn_ball(right)
        else:
            ball_vel[0]=-ball_vel[0]
            ball_vel[0]=ball_vel[0]*2
            ball_vel[1]=ball_vel[1]*2    
    if (ball_pos[0]==(width-pad_width-ball_radius)):
        if (ball_pos[1]<=pad2_pos[1] or ball_pos[1]>=(pad2_pos[1]+80)):
            score1+=1
            spawn_ball(left)
        else:
            ball_vel[0]=-ball_vel[0]
            ball_vel[0]=ball_vel[0]*2
            ball_vel[1]=ball_vel[1]*2  
#Draw Handler
def draw(canvas):
    global score1, score2, pad1_pos, pad2_pos
    global ball_pos, ball_vel
    # draw mid line and gutters
    canvas.draw_text("By MrL",[525,395],20,"white")
    canvas.draw_line([width / 2, 0],[width / 2, height], 1, "White")
    canvas.draw_line([pad_width, 0],[pad_width, height], 1, "White")
    canvas.draw_line([width - pad_width, 0],[width - pad_width, height], 1, "White")
    # update ball
    update_ball()
    # draw ball
    canvas.draw_circle(ball_pos,ball_radius,3,"Grey","White")
    # Paddle1 Postion Update
    pad1_pos[1]+=pad1_vel
    if (pad1_pos[1]<0):
        pad1_pos[1]=0
    elif (pad1_pos[1]>320):
        pad1_pos[1]=320
    # Paddle2 Postion Update
    pad2_pos[1]+=pad2_vel
    if (pad2_pos[1]<0):
        pad2_pos[1]=0
    elif (pad2_pos[1]>320):
        pad2_pos[1]=319
    # draw paddles
    canvas.draw_line([pad1_pos[0],pad1_pos[1]],[0,pad1_pos[1]+pad_height],pad_width+5,player1_colour)
    canvas.draw_line([pad2_pos[0]+5,pad2_pos[1]+5],[width-pad_width+5,pad2_pos[1]+pad_height+5],pad_width+3,player2_colour)
    # draw scores
    canvas.draw_text(player1_name+'   '+str(score1),[90,80],25,"White")
    canvas.draw_text(player2_name+'   '+str(score2),[390,80],25,"White")
    # Declare winner
    if (time%5==0 or time%2==0):
        if (score1>=5 or score2>=5):
            if (score1>=score2):
                canvas.draw_text(player1_name+' Wins',[80,250],30,"teal")
            if (score2>=score1):
                canvas.draw_text(player2_name+' Wins',[380,250],30,"teal")
  
# Colour Choice
def colour1(colour):
    global player1_colour
    player1_colour=colour
    
# Colour Choice
def colour2(colour):
    global player2_colour
    player2_colour=colour

# Winner
def spot_time():
    global time
    time+=1
    
# Setting Paddle Velocity    
def keydown(key):
    global pad1_vel, pad2_vel
    if (key==38):
        pad2_vel=-10
    elif (key==40):
        pad2_vel=10
    elif (key==87):
        pad1_vel=-10
    elif (key==83):
        pad1_vel=10
   
# Resetting paddle Velocity
def keyup(key):
    global pad1_vel, pad2_vel
    if (key==38):
        pad2_vel=0
    elif (key==40):
        pad2_vel=0
    elif (key==87):
        pad1_vel=0
    elif (key==83):
        pad1_vel=0

# create frame
frame = simplegui.create_frame("Pong", width, height)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_label("Enter your Names ")
player1_n=frame.add_input("Player 1",play1,200)
colour1_n=frame.add_input("Colour of Player 1 ",colour1,200)
player2_n=frame.add_input("Player 2",play2,200)
colour2_n=frame.add_input("Colour of Player 2 ",colour2,200)
frame.add_label("Click New Game.")
frame.add_button("New Game",new_game,200)
frame.add_label("To Restart Click New Game.")
timer=simplegui.create_timer(100,spot_time)

# start frame
#new_game()
timer.start()
frame.start()

