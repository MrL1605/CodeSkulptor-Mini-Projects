#http://www.codeskulptor.org/#user29_bcQGQKnWaSLISLx.py

#Magic Circle
#import modules
import simplegui 

# Define globals
HEIGHT = 400
WIDTH = 400
RADIUS_INCREMENT = 5
ball_radius = 40
lalit="By MrL"

# Draw handler
def draw(canvas):
    canvas.draw_circle([200,200],ball_radius,10,"BLUE","White")
    canvas.draw_circle([200,200],ball_radius-20,10,"red","yellow")
    canvas.draw_text(lalit, [340,380], 15, "RED")
    
# Event handlers for buttons
def increase_radius ():
    global ball_radius
    ball_radius+=1
    m_label.set_text("Radius = "+str( ball_radius))
    
def decrease_radius():
    global ball_radius
    if (ball_radius<=25):
        ball_radius=25
    else:
        ball_radius-=1
    m_label.set_text("Radius = "+str( ball_radius))
    
# Create frame and assign callbacks to event handlers
frame = simplegui.create_frame("Ball control", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
m_label=frame.add_label("Radius = "+str( ball_radius))
frame.add_button("Increase radius", increase_radius)
frame.add_button("Decrease radius", decrease_radius)
label2=frame.add_label("Description:")
label3=frame.add_label("Increase/Decrease the radius as desired.It won't decrease after a certain limit.\n\n")
label4=frame.add_label("Observe that as the radius of circle increases black frame starts shaking...")                        
label5=frame.add_label("Concentrate on the innner of yellow circle there is magic in it.")                        

# Start the frame animation
frame.start()


