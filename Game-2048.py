#http://www.codeskulptor.org/#user34_Ps5GNRIgIkBbBtN.py

"""
Clone of 2048 game.
"""
import poc_2048_gui        
import random

# Directions, DO NOT MODIFY
UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4

# Offsets for computing tile indices in each direction.
# DO NOT MODIFY this dictionary.    
OFFSETS = {UP: (1, 0), 
           DOWN: (-1, 0), 
           LEFT: (0, 1), 
           RIGHT: (0, -1)} 
   
def merge(line):
    """
    Helper function that merges a single row or column in 2048
    """
    
    #Arrages the line in order and shifts the zeros to the right    
    _value_position=0
    _d_line=line
    #This loop used to iterate line lenght of line times
    for _dummy_n in range(len(line)):
        _value_position=0
        _d_line=line
        for _tile in _d_line:
            if _tile==0:
                _d_pos=_value_position
                while _d_pos!=(len(line)-1):
                    line[_d_pos]=line[_d_pos+1]
                    _d_pos+=1
                else :
                    line[-1]=0
            _d_line=line
            _value_position+=1
            
    #Combines the two equal tiles
    _status=[]
    _value_position=0
    _d_line=line
    
    #This loop is used to create a status list of Boolean varaiabes
    for _dummy_n in range(len(line)):
        _status.append(False)
    _value_position=0
    _d_line=line
    #d_line is duplicate of tile to operate it in this loop
    for _tile in _d_line:
        if _value_position!=(len(line)-1):
            if ((_tile==line[_value_position+1]) and (_status[_value_position]==False)):
                _status[_value_position]=True
                line[_value_position]=line[_value_position]+line[_value_position+1]
                _d_pos=_value_position+1
                while _d_pos != (len(line)-1):
                    line[_d_pos]=line[_d_pos+1]
                    _d_pos+=1
                else:
                    line[_d_pos]=0
            _d_line=line
            _value_position+=1  
    #Actually line itself is modified and there is no need for return statement
    #But for testing purpose
    return line
    
#Class TwentyForty
class TwentyFortyEight:
    """
    Class to run the game logic.
    """

    def __init__(self, grid_height, grid_width):
        #Initialses all the class variables
        self.grid_height=grid_height
        self.grid_width=grid_width
        self.tile=[]
        self.reset()

    def reset(self):
        """
        Reset the game so the grid is empty.
        """
        #Reset the tile to NULL list
        self.tile=[]
        
        #Add required number of zeros in the tile_grid 
        for _dummy_height in range (self.grid_height):
            _row=[]
            for dummy_width in range(self.grid_width):
                _row.append(0)
            self.tile.extend([_row])
        
    def __str__(self):
        """
        Return a string representation of the grid for debugging.
        """
        #Return a string representation of the grid for debugging.
        return str(self.tile)

    def get_grid_height(self):
        """
        Get the height of the board.
        """
        #Get the height of the board.
        return self.grid_height
    
    def get_grid_width(self):
        """
        Get the width of the board.
        """
        #Get the width of the board.
        return self.grid_width
    
    def _move_helper_down(self,direction):
        """
        Helps to decrease number of lines in move function 
        specially in UP and DOWN directions  
        """
        #Creating two lists to track the lists 
        #which are passed to merge function 
        _dummy_line=[]
        _old_dummy_line=[]
        
        for _line_num in range(self.grid_width):
                _dummy_line.append([])
                _old_dummy_line.append([])
#            print dummy_line
            #Creating Lines taking elements from self.tile
        for _line_num in range(self.grid_width):
            for _line_element in range(self.grid_height):
#               print self.tile[line_element][line_num],line_num,line_element
                _dummy_line[_line_num].append(self.tile[_line_element][_line_num])
                _old_dummy_line[_line_num].append(self.tile[_line_element][_line_num])
#          	print dummy_line,'after adding elements'
            #First reversing the generated line
        for _line_num in range(self.grid_width):    
            if direction == DOWN:
                _dummy_line[_line_num].reverse()
            #passing every line through merge function
            merge(_dummy_line[_line_num])
            #Secondly in reversed, reverses the line again
            if direction == DOWN:
                _dummy_line[_line_num].reverse()
#            print dummy_line,'after using merge'
            
        #Setting a boolean varible to check weather to set a new tile or not 
        _set_new_tile=False
            
        #Loop to detect wether there is change in lines or not
        for _line_num in range(self.grid_width):
            for _line_element in range(self.grid_height):
                 self.tile[_line_element][_line_num]=_dummy_line[_line_num][_line_element]
                 #If there is change set the set_new_tile variable to True
                 if _old_dummy_line!=_dummy_line:
                    _set_new_tile=True
#            print dummy_line
#            print self.tile,'tile'
            #If set_new_tile is True Create a new tile with a random value 
        if _set_new_tile==True:
            for _line_num in range(self.grid_width):
                for _line_element in range(self.grid_height):                                     
                    self.set_tile(_line_element,_line_num,self.tile[_line_element][_line_num])    
            self.new_tile() 

    def _move_hepler_right(self,direction):
        """
        Helps to decrease number of lines in move function 
        specially in UP and DOWN directions  
        """
        #creating lists inside a list for different lines 
        _dummy_line=[]
        _old_dummy_line=[]
        #creating lists inside a list for different lines 
        #to be passed to merge function
#       print dummy_line
        for _line_num in range(self.grid_height):
            _dummy_line.append([])
            _old_dummy_line.append([])
#       print dummy_line
        #Creating Lines taking elements from self.tile
        for _line_num in range(self.grid_height):
           for _line_element in range(self.grid_width):
#              print self.tile[line_num][line_element],line_num,line_element
               _dummy_line[_line_num].append(self.tile[_line_num][_line_element])
               _old_dummy_line[_line_num].append(self.tile[_line_num][_line_element])                
#          print dummy_line,'after adding elements'
           #First reversing the generated line                
        for _line_num in range(self.grid_height):             
           if direction == RIGHT:
               _dummy_line[_line_num].reverse()
           #passing every line through merge function
           merge(_dummy_line[_line_num])
           #Secondly in reversed, reverses the line again
           if direction == RIGHT:
               _dummy_line[_line_num].reverse()
#       print dummy_line,'after using merge'
        #Setting a boolean varible to check weather to set a new tile or not 
        _set_new_tile=False
            
        #Loop to detect wether there is change in lines or not
        for _line_num in range(self.grid_height):
            for _line_element in range(self.grid_width):
                self.tile[_line_num][_line_element]=_dummy_line[_line_num][_line_element]
                #If there is change set the set_new_tile variable to True
                if _old_dummy_line!=_dummy_line:
                    _set_new_tile=True
#        print dummy_line
#        print self.tile,'tile'
        #If set_new_tile is True Create a new tile with a random value 
        if _set_new_tile==True:
            self.new_tile()                     
            for _line_num in range(self.grid_height):
                for _line_element in range(self.grid_width):  
                    self.set_tile(_line_num,_line_element,self.tile[_line_num][_line_element])    

            
    def move(self, direction):
        """
        Move all tiles in the given direction and add
        a new tile if any tiles moved.
        """
        #By IF-ELSE method
        
        #Detects the direction and starts further imlementation 
        if direction == DOWN or direction==UP:
            #creating lists inside a list for different lines 
            #to be passed to merge function
            self._move_helper_down(direction)
                            
        #Creating two lists to track the lists 
        #which are passed to merge function 
        
#        print dummy_line
        elif direction == RIGHT or direction == LEFT:
            self._move_hepler_right(direction)                                     
    
    def new_tile(self):
        """
        Create a new tile in a randomly selected empty 
        square.  The tile should be 2 90% of the time and
        4 10% of the time.
        """
        #Creating a variable randi which has range[0,1) with one decimal
        #Probabilty of every number is equal
        _randi = random.random()
        
        #But probabilty of decimals less than 0.9 is greater than that of occuring 0.1
        if _randi < .9:
            _value = 2
        else:
            _value = 4
            
        #Creating a varible to determine wether or not to create a new tile.
        #Creating an empty list of positions where element is zero.
        _imp_list=[]
        
        #Adding positions to the list where elements are zero. 
        for _random_height in range(self.grid_height):
            for _random_width in range (self.grid_width):
                if (self.tile[_random_height][_random_width]==0):	
                    _imp_list.append([_random_height,_random_width])
        #If there are element it zero value
        if _imp_list!=[]:
            _value_position=random.choice(_imp_list)
            #Create a new tile with value        
            self.set_tile(_value_position[0],_value_position[1],_value)             
              
    def set_tile(self, row, col, value):
        """
        Set the tile at position row, col to have the given value.
        """ 
        #Set the tile at position row, col to have the given value.
        self.tile[row][col]=value

    def get_tile(self, row, col):
        """
        Return the value of the tile at position row, col.
        """      
        #Return the value of the tile at position row, col
        return self.tile[row][col] 
    
poc_2048_gui.run_gui(TwentyFortyEight(5, 4))

# Phase 1
#import user34_hbhMz0FBOi_1 as merge_test
#merge_test.run_test(merge)

# Phase 2
#import user34_sw90o8thMp_1 as tile_test
#tile_test.run_test(TwentyFortyEight)

# Phase 3
#import user34_B88RxBpJcx_0 as poc_2048_testsuite
#poc_2048_testsuite.run_test(merge, TwentyFortyEight)



