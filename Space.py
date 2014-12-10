#http://www.codeskulptor.org/#user33_CKLVtBCU9ntSKfv.py

# Spaceship
# By MrL

import simplegui
import math
import random

# globals for user interface
WIDTH = 800
HEIGHT = 600
score = 0
t_score=[]
lives = 3
time = 0.5
start_flag=True

class ImageInfo:
    def __init__(self, center, size, radius = 0, lifespan = None, animated = False):
        self.center = center
        self.size = size
        self.radius = radius
        if lifespan:
            self.lifespan = lifespan
        else:
            self.lifespan = float('inf')
        self.animated = animated

    def get_center(self):
        return self.center

    def get_size(self):
        return self.size

    def get_radius(self):
        return self.radius

    def get_lifespan(self):
        return self.lifespan

    def get_animated(self):
        return self.animated

if True:    
    # art assets created by Kim Lathrop, may be freely re-used in non-commercial projects, please credit Kim
        
    # debris images - debris1_brown.png, debris2_brown.png, debris3_brown.png, debris4_brown.png
    #                 debris1_blue.png, debris2_blue.png, debris3_blue.png, debris4_blue.png, debris_blend.png
    debris_info = ImageInfo([320, 240], [640, 480])
    debris_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/debris2_blue.png")

    # nebula images - nebula_brown.png, nebula_blue.png
    nebula_info = ImageInfo([400, 300], [800, 600])
    nebula_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/nebula_blue.s2014.png")

    # splash image
    splash_info = ImageInfo([200, 150], [400, 300])
    splash_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/splash.png")

    # ship image
    ship_info = ImageInfo([45, 45], [90, 90], 35)
    ship_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/double_ship.png")

    # missile image - shot1.png, shot2.png, shot3.png
    missile_info = ImageInfo([5,5], [10, 10], 3, 20)
    missile_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/shot2.png")

    # asteroid images - asteroid_blue.png, asteroid_brown.png, asteroid_blend.png
    asteroid_info = ImageInfo([45, 45], [90, 90], 40)
    asteroid_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/asteroid_blue.png")

    # animated explosion - explosion_orange.png, explosion_blue.png, explosion_blue2.png, explosion_alpha.png
    explosion_info = ImageInfo([64, 64], [128, 128], 17, 24, True)
    explosion_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/explosion_alpha.png")

    # sound assets purchased from sounddogs.com, please do not redistribute
    soundtrack = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/soundtrack.mp3")
    missile_sound = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/missile.mp3")
    missile_sound.set_volume(0.5)
    ship_thrust_sound = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/thrust.mp3")
    ship_thrust_sound.set_volume(1)
    explosion_sound = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/explosion.mp3")

# helper functions to handle transformations
def angle_to_vector(ang):
    return [math.cos(ang), math.sin(ang)]

def dist(p,q):
    return math.sqrt((p[0] - q[0]) ** 2+(p[1] - q[1]) ** 2)

# Ship class
class Ship:
    def __init__(self, pos, vel, angle, image, info):
        self.pos = [pos[0],pos[1]]
        self.vel = [vel[0],vel[1]]
        self.thrust = False
        self.angle = angle
        self.angle_vel = 0
        self.image = image
        self.image_center = info.get_center()
        self.image_size = info.get_size()
        self.radius = info.get_radius()
        self.th_cons=8.1
        self.fr_cons=0.03
        
    def draw(self,canvas):
        if self.thrust:
            canvas.draw_image(self.image, [self.image_center[0]+90,self.image_center[1]], self.image_size,self.pos, self.image_size,self.angle)
            ship_thrust_sound.play()
        else:    
            canvas.draw_image(self.image, self.image_center, self.image_size, self.pos, self.image_size,self.angle)
        
    def update(self):
        self.angle+=self.angle_vel
        self.vel[0]*=(1-self.fr_cons)
        self.vel[1]*=(1-self.fr_cons)
        if self.thrust:
            forward=angle_to_vector(self.angle)
            self.vel[0]=forward[0]*(self.th_cons)
            self.vel[1]=forward[1]*(self.th_cons)
            ship_thrust_sound.play()
        if (self.pos[0]<0):
            self.pos[0]=(WIDTH-5)
        if (self.pos[0]>WIDTH):
            self.pos[0]=(5)
        if (self.pos[1]<0):
            self.pos[1]=HEIGHT-5
        if (self.pos[1]>HEIGHT):
            self.pos[1]=5
        for i in range(2):
            self.pos[i]+=self.vel[i]
     
    def shoot(self):
        global group_missile
        forward=angle_to_vector(self.angle)
        a_missile = Sprite([self.pos[0]+forward[0]*45,self.pos[1]+forward[1]*45], 
                           [(forward[0]*45)*0.3,(forward[1]*45)*0.3], 
                           0, 0, missile_image, missile_info, missile_sound)     
        group_missile.add(a_missile)
        
# Sprite class
class Sprite:
    def __init__(self, pos, vel, ang, ang_vel, image, info, sound = None):
        self.pos = [pos[0],pos[1]]
        self.vel = [vel[0],vel[1]]
        self.angle = ang
        self.angle_vel = ang_vel
        self.image = image
        self.image_center = info.get_center()
        self.image_size = info.get_size()
        self.radius = info.get_radius()
        self.lifespan = info.get_lifespan()
        self.animated = info.get_animated()
        self.age = 0
        if sound:
            sound.rewind()
            sound.play()
        
    def draw(self, canvas):
        if (self.animated):
            print "true"
            explosion_sound.rewind()
            explosion_sound.play()
            #while(self.age<=self.lifespan):
            canvas.draw_image(self.image, [self.image_center[0]+128*self.age,self.image_center[1]], 
                              self.image_size, self.pos, self.image_size,self.angle)
                
            self.age+=1
        else: 
            canvas.draw_image(self.image, self.image_center, self.image_size,self.pos, self.image_size,self.angle)	

    def update(self):
        self.angle+=self.angle_vel
        if (self.pos[0]<=0 or self.pos[0]>=WIDTH):
            self.pos[0]=WIDTH-self.pos[0]
        if (self.pos[1]<=0 or self.pos[1]>=HEIGHT):
            self.pos[1]=HEIGHT-self.pos[1]
        for i in range(2):
            self.pos[i]+=self.vel[i]  
        self.age+=1
        if (self.age>=self.lifespan):
            return True
        return False
            
            
    def collide(self,other_object):
        if ((dist(self.pos,other_object.pos)-self.radius-other_object.radius)<=0):
            return True
        else: 
            return False
 
# Draw handler        
def draw(canvas):
    global time,group_rock,group_missile,my_ship,lives, score,start_flag,group_explosion,t_score
    # animiate background
    time += 1
    wtime = (time / 4) % WIDTH
    center = debris_info.get_center()
    size = debris_info.get_size()
    canvas.draw_image(nebula_image, nebula_info.get_center(), nebula_info.get_size(),[WIDTH / 2, HEIGHT / 2], [WIDTH, HEIGHT])
    canvas.draw_image(debris_image, center, size, (wtime - WIDTH / 2, HEIGHT / 2), (WIDTH, HEIGHT))
    canvas.draw_image(debris_image, center, size, (wtime + WIDTH / 2, HEIGHT / 2), (WIDTH, HEIGHT))
    # splash Screen
    if (start_flag==True):
        canvas.draw_image(splash_image, splash_info.get_center(), splash_info.get_size(),[WIDTH / 2, HEIGHT / 2], splash_info.get_size())    
    else:
        # draw ship and sprites
        my_ship.draw(canvas)
        process_sprite_group(canvas,group_rock)
        process_sprite_group(canvas,group_missile)
        process_sprite_group(canvas,group_explosion)
        
        # update ship and sprites
        my_ship.update()
        # update lives and score
        if (group_collide(group_rock,my_ship)):
            lives-=1
        score+=group_group_collide(group_missile,group_rock)
        if (lives<=0):
            print "score",score
            print 
            t_score.append(score)
            if len(t_score)!=0:
                frame.add_label("Score was "+str(t_score[-1]))
            print''
            print 'New Game'
            start_flag=True
            soundtrack.pause()	        
    canvas.draw_text ('Lives  '+str(lives),[WIDTH-100,30],25,"whITE")
    canvas.draw_text ('Score  '+str(score),[30,30],25,"WHITE")
            
# timer handler that spawns a rock
def rock_spawner():
    global group_rock
    if (len(group_rock)<=12):
        a_rock = Sprite([random.randrange(50,WIDTH-50),random.randrange(50,HEIGHT-50)], 
                        [random.randrange(-1,1),random.randrange(-1,1)], 
                         0,random.choice([-0.05,0.05]), asteroid_image, asteroid_info)     
        while(dist(a_rock.pos,my_ship.pos)<=a_rock.radius+50):
            a_rock = Sprite([random.randrange(50,WIDTH-50),random.randrange(50,HEIGHT-50)], 
                           [random.randrange(-1,1),random.randrange(-1,1)], 
                            0,random.choice([-0.05,0.05]), asteroid_image, asteroid_info)
        group_rock.add(a_rock)
        
# helper funciton for rock
def process_sprite_group(canvas,group):
    for i in list(group):
        i.draw(canvas)
        if i.update():
            group.remove(i)     

# groups collide function        
def group_collide(group,other_object):
    global group_explosion
    for j in list(group):
        if j.collide(other_object):
            group.discard(j)
            a_explosion=Sprite(j.pos, j.vel, 0,0, explosion_image, explosion_info)  
            print "after g c",j.pos
            group_explosion.add(a_explosion)
            return True
def group_group_collide(group,group2):
    rm=set([])
    copy_group=group
    for i in copy_group:
        if (group_collide(group2,i)):
            rm.add(i)
            print "after g g c",i.pos
            group.discard(i)
    return len(rm)
        
# keyhandlers 
def kd(key):
    global my_ship
    if not start_flag:
        if (key==39):
            my_ship.angle_vel=0.06
        elif (key==37):
            my_ship.angle_vel=-0.06
        if (key==38):
            my_ship.thrust=True      
        if (key==32):
            my_ship.shoot()      
def ku(key):
    global my_ship
    if (key==39 or key==37):
        my_ship.angle_vel=0
    elif (key==38):
        my_ship.thrust=False
        ship_thrust_sound.pause()
    
# mouse click handler
def start_screen(pos):
    global start_flag,score,lives,time,my_ship,group_missile,group_rock,group_explosion
    if start_flag:
        score = 0
        lives = 3
        time = 0.5
        group_rock = set([])
        group_missile =set([])
        group_explosion=set([])
        my_ship = Ship([WIDTH / 2, HEIGHT / 2], [0.0, 0.0], 0.0, ship_image, ship_info)
        start_flag=False
        # sound track
        soundtrack.rewind()
        soundtrack.play()
        timer.start()
        
# initialize frame
frame = simplegui.create_frame("Asteroids", WIDTH, HEIGHT)

# initialize ship and two sprites
my_ship = Ship([WIDTH / 2, HEIGHT / 2], [0.0, 0.0], 0.0, ship_image, ship_info)
group_rock = set([])
group_missile =set([])
group_explosion=set([])

# register handlers
frame.set_draw_handler(draw)
frame.set_keydown_handler(kd)
frame.set_keyup_handler(ku)
frame.set_mouseclick_handler(start_screen)
timer = simplegui.create_timer(1000.0, rock_spawner)

# get things rolling
frame.start()


