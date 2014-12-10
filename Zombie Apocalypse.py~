#http://www.codeskulptor.org/#user36_k9uJUj7IYJcsrLR_0.py

"""
Student portion of Zombie Apocalypse mini-project
"""

import random
import poc_grid
import poc_zombie_gui
import poc_queue
#Test suite for mini project
#import user35_7MSl6axrsDU3iXs as poc_zombie_gui

# global constants
EMPTY = 0 
FULL = 1
FOUR_WAY = 0
EIGHT_WAY = 1
OBSTACLE = "obstacle"
HUMAN = "human"
ZOMBIE = "zombie"


class Zombie(poc_grid.Grid):
    """
    Class for simulating zombie pursuit of human on grid with
    obstacles
    """

    def __init__(self, grid_height, grid_width, obstacle_list = None, 
                 zombie_list = None, human_list = None):
        """
        Create a simulation of given size with given obstacles,
        humans, and zombies
        """
        poc_grid.Grid.__init__(self, grid_height, grid_width)
        if obstacle_list != None:
            for cell in obstacle_list:
                self.set_full(cell[0], cell[1])
        if zombie_list != None:
            self._zombie_list = list(zombie_list)
        else:
            self._zombie_list = []
        if human_list != None:
            self._human_list = list(human_list)  
        else:
            self._human_list = []
        
    def clear(self):
        """
        Set cells in obstacle grid to be empty
        Reset zombie and human lists to be empty
        """
        self._human_list = []
        self._zombie_list = []
        poc_grid.Grid.clear(self)
        
    def add_zombie(self, row, col):
        """
        Add zombie to the zombie list
        """
        self._zombie_list.append((row,col))
                
    def num_zombies(self):
        """
        Return number of zombies
        """
        return len(self._zombie_list)  
          
    def zombies(self):
        """
        Generator that yields the zombies in the order they were
        added.
        """
        # replace with an actual generator
        for item in self._zombie_list:
            yield item

    def add_human(self, row, col):
        """
        Add human to the human list
        """
        self._human_list.append((row,col))
        
    def num_humans(self):
        """
        Return number of humans
        """
        return len(self._human_list)
    
    def humans(self):
        """
        Generator that yields the humans in the order they were added.
        """
        # replace with an actual generator
        for item in self._human_list:
            yield item
        
    def compute_distance_field(self, entity_type):
        """
        Function computes a 2D distance field
        Distance at member of entity_queue is zero
        Shortest paths avoid obstacles and use distance_type distances
        """
        #while boundary is not empty:
        #	current_cell  ←  dequeue boundary
        #	for all neighbors neighbor_cell of current_cell:
        #		if neighbor_cell is not in visited:
        #			add neighbor_cell to visited
        #			enqueue neighbor_cell onto boundary
        visited = poc_grid.Grid(self.get_grid_height(), self.get_grid_width())
        distance_field= []
        boundary = poc_queue.Queue()
        for _dum_x in range(self.get_grid_height()):
            distance_field.append([])
            for _dum_y in range(self.get_grid_width()):
                distance_field[-1].append(self.get_grid_height()*self.get_grid_width())                
        if entity_type=='zombie':
            for zom in self.zombies():
                boundary.enqueue(zom)
                visited.set_full(zom[0],zom[1])
                distance_field[zom[0]][zom[1]]=0
        elif entity_type=='human':
            for hum in self.humans():
                boundary.enqueue(hum)
                visited.set_full(hum[0],hum[1])
                distance_field[hum[0]][hum[1]]=0
                
        while boundary.__len__() > 0:
            curr_cell = boundary.dequeue()
            distance=distance_field[curr_cell[0]][curr_cell[1]]+1
            neighbors = self.four_neighbors(curr_cell[0], curr_cell[1])
            #neighbors = self.eight_neighbors(curr_cell[0], curr_cell[1])
            for neighbor in neighbors:
                if visited.is_empty(neighbor[0], neighbor[1]):
                    visited.set_full(neighbor[0], neighbor[1])
                    if self.is_empty(neighbor[0],neighbor[1]):
                        boundary.enqueue(neighbor)
                        distance_field[neighbor[0]][neighbor[1]] = distance
        return distance_field
            
    def move_humans(self, zombie_distance):
        """
        Function that moves humans away from zombies, diagonal moves
        are allowed
        """
        #print zombie_distance,'zom_distance'
        #print self._human_list,'human_list'
        for human in self.humans():
            #print human,'curr_human'
            _index=self._human_list.index(human)
            neighbors = self.eight_neighbors(human[0], human[1])
            max_distance = 0
            for neighbor in neighbors:
                distance = zombie_distance[neighbor[0]][neighbor[1]]
                #print distance,neighbor,'all neighbors'
                if distance > max_distance and distance!=self.get_grid_height()*self.get_grid_width():
                    max_distance = distance
            #print max_distance,'max_distance'
            for neighbor in neighbors:
                distance = zombie_distance[neighbor[0]][neighbor[1]]
                if distance==max_distance:
                    #print neighbor,'max_neighbor'
                    self._human_list[_index] = (neighbor[0],neighbor[1])
        #print self._human_list,'hman_list'
        
        
    def move_zombies(self, human_distance):
        """
        Function that moves zombies towards humans, no diagonal moves
        are allowed
        """
        #print human_distance,'human_distance'
        #print self._zombie_list
        for zombie in self.zombies():
            #print zombie,'curr_zombie'
            _index=self._zombie_list.index(zombie)
            neighbors = self.four_neighbors(zombie[0], zombie[1])
            min_distance = human_distance[zombie[0]][zombie[1]]
            for neighbor in neighbors :
                distance = human_distance[neighbor[0]][neighbor[1]]
                #print distance,neighbor,'all neighbors'
                if distance < min_distance and distance!=self.get_grid_height()*self.get_grid_width():
                    min_distance = distance
            #print min_distance,'min_distance'
            for neighbor in neighbors:
                distance = human_distance[neighbor[0]][neighbor[1]]
                if distance==min_distance:
                    #print neighbor,'min_neighbor'
                    self._zombie_list[_index] = (neighbor[0],neighbor[1])
        #print self._zombie_list
        
#Owl test failure!!!!!!        
#self, grid_height, grid_width, obstacle_list = None, 
#                 zombie_list = None, human_list = None):
#obj = Zombie(3, 3, [], [(1, 1)], [(2, 2)])
#for zom in obj.zombies():
#    print zom
#dist = [[4, 3, 2], [3, 2, 1], [2, 1, 0]] 
#obj.move_zombies(dist) 
#for zom in obj.zombies():
#    print zom

#expected location to be one of [(1, 2), (2, 1)] but received (1, 1)        
        
# Start up gui for simulation - You will need to write some code above
# before this will work without errors

#poc_zombie_gui.run_gui(Zombie(30, 40))
#game = Zombie(30, 40)
#poc_zombie_gui.run_gui(game)
#import simplegui
#
#def timer_handler():
#    game.move_humans(game.compute_distance_field(ZOMBIE))
#    game.move_zombies(game.compute_distance_field(HUMAN))
#
#timer = simplegui.create_timer(1000, timer_handler)
#timer.start()

#When we do a breadth first search, we are describing an approach to visit every cell in a grid.
#So the visited are simply the cells which have been searched. In the case of the wildfire demo,
#there are three kind of cells, the ones which aren't on fire (unvisited), the ones next to the
#fire (being visited, which means they are in the boundary queue), and the ones on fire (which 
#have been visited). All the search does is turn a boundary cell into a visited cell and put all
#the new boundary cells into the queue (setting them up to be visited in short order). Think of
#it as going round-and-round in an every expanding circle, with the circle expanding from one 
#cell into its neighbors.
#
#The distance_field is a grid. In other words, its a list of lists [[ ], [ ], [ ].. ]. What we 
#do in Zombie Apocalypse is start with a boundary, made up of lets say Zombies, and the 
#corresponding distance_field. So if the Zombies are in a 3x3 grid, then the distance_field will
#be a list of three lists (and per instruction, would be initialized to [[9, 9, 9], [9, 9, 9], 
#[9, 9, 9]].
#
#Next, we note in the distance_field the distance for all cells which are occupied by zombies, 
#which would be 0. If there was a zombie at (2, 0), we would update the distance_field to 
#[[9, 9, 9], [9, 9, 9], [0, 9, 9]]. So then what happens..
#
#We dequeue a zombie (with distance 0). In this case (2,0). We burn the cell (think wildfire), 
#we enqueue the boundary cells (determined by the four neighbors .. these are the cells we will
#burn next) and we log the distance of each of these boundary cells into the distance_field. 
#The distance is +1 from the cell which each neighbor borders. So the next iteration to distance
#_field would look like [[9, 9, 9], [1, 9, 9], [0, 1, 9]].
#
#Of course, these neighbor cell could already have been neighbored by a difference cell started 
#by a difference zombie. If the already logged distance is less than the new distance +1, then 
#we don't log a new distance.
#
#Also remember, never burn an obstacle.

#import user35_DE7mSBa91a_15 as test
#test.run_test(Zombie)

#import user35_TWcHt32AmbBZMcb_33 as tests
#tests.test_zombie(Zombie)    

#import user35_EPZOWWGoUeaEemm as test
#test.phase1_test(Zombie)
#test.phase2_test(Zombie)
#test.phase3_test(Zombie)
