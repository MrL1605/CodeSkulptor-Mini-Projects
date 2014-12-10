#http://www.codeskulptor.org/#user35_ohtWniuDtv05jvK_11.py

"""
Monte Carlo Tic-Tac-Toe Player
"""

import random
import poc_ttt_gui
import poc_ttt_provided as provided

# Constants for Monte Carlo simulator
# Change as desired
NTRIALS = 3   # Number of trials to run
MCMATCH = 2.0  # Score for squares played by the machine player
MCOTHER = 1.0  # Score for squares played by the other player
EMPTY = 1
PLAYERX = 2
PLAYERO = 3 
DRAW = 4
# Add your functions here.
# Some Helper Function
def switch_player(player):
    """
    Convenience function to switch players.
    
    Returns other player.
    """
    if player == PLAYERX:
        return PLAYERO
    else:
        return PLAYERX
    
#return nothing
def mc_trial( board, player):
    """
    The function plays a game, starting with the given player by making 
    random moves, alternating between players. The function returns when 
    the game is over. The modified board contains the state of the game
    """
    board_grid_list=range(board.get_dim())
    winner = board.check_win()
    while(winner == None):    
        randxpos=random.choice(board_grid_list)
        randypos=random.choice(board_grid_list)
        board.move(randxpos, randypos, player)
        player = switch_player(player)
        winner = board.check_win()

def adding_scores( board, scores, player, xpos, ypos, win):
    """
    Updates the Scores list and simplifies the mc_update function.
    """
    if (win==True):
        if (board.square(xpos, ypos) == EMPTY):
            scores[xpos][ypos] += 0.0
        elif (board.square(xpos, ypos) == player):
            scores[xpos][ypos] += (MCMATCH)
        else:
            scores[xpos][ypos] += (-MCOTHER)
    else:
        if (board.square(xpos, ypos) == EMPTY):
            scores[xpos][ypos] += 0.0
        elif (board.square(xpos, ypos) == player):
            scores[xpos][ypos] += (-MCMATCH)
        else:
            scores[xpos][ypos] += (MCOTHER)
            
#return nothing
def mc_update_scores( scores, board, player): 
    """
    Function takes a grid of scores, a board from a completed game, and 
    which player the machine player is. Function should score the completed 
    board and update the scores grid. The function updates the scores grid directly.
    """
    winner=board.check_win()
    if (player == winner):
        for xpos in range(board.get_dim()):
            for ypos in range(board.get_dim()):
                adding_scores( board, scores, player, xpos, ypos, True)
    elif (winner == DRAW ):
        # Almost Does nothing
        pass
    else:
        for xpos in range(board.get_dim()):
            for ypos in range(board.get_dim()):
                adding_scores( board, scores, player, xpos, ypos, False)

def max_score_in_2d_list ( scores, given_list ):    
    """
    Determines the greatest score in given 2D list 
    """
    max_value = scores[given_list[0][0]][given_list[0][1]]
    for empty in given_list:
        if (scores[empty[0]][empty[1]] >= max_value ):
            max_value = scores[empty[0]][empty[1]]
    return max_value
    
#returns best_move
def get_best_move(board, scores):
    """
    Function takes a current board and scores. Function find all of the
    empty squares with the maximum score and randomly return one of them.
    The case where the board is full will not be tested.
    """
    if (board.get_empty_squares() == []):
        return
    empty_squares = board.get_empty_squares()
    max_list = []
    max_value = max_score_in_2d_list ( scores, empty_squares )
    for empty in empty_squares:
        if ( scores[empty[0]][empty[1]] == max_value ):
            max_list.append(empty)
    empty = random.choice (max_list)
    return empty
    
    
def mc_move(board, player, trials):
    """
    Function takes a current board, machine player, and the number of trials. 
    Function uses the Monte Carlo simulation to return a move for the machine
    player in the form of a tuple.
    """
    scores = []
    temp_board = board.clone()
    for xpos in range(board.get_dim()):
        scores.append([])
        for ypos in range(board.get_dim()):
            scores[xpos].append(0*ypos)
    
    for _dummy_trails in range(trials):
        mc_trial( temp_board, player)
        mc_update_scores( scores, temp_board, player )	      
#    print scores,get_best_move(board,scores)
    return get_best_move(board,scores)

# Test game with the console or the GUI.
# Uncomment whichever you prefer.
# Both should be commented out when you submit for
# testing to save time.

#provided.play_game(mc_move, NTRIALS, False)        
#poc_ttt_gui.run_gui(3, provided.PLAYERX, mc_move, NTRIALS, False)


# Test suite for individual functions
#import user34_Uc9ea2tRiN_0 as test_ttt
#test_ttt.test_trial(mc_trial)
#print
#test_ttt.test_update_scores(mc_update_scores, MCMATCH, MCOTHER)
#print
#test_ttt.test_best_move(get_best_move)

#[-8.3 pts] mc_move(TTTBoard(3, False, [[PLAYERX, EMPTY, EMPTY], [PLAYERO, PLAYERO, EMPTY], [EMPTY, PLAYERX, EMPTY]]), PLAYERX, NTRIALS) returned mostly bad moves: [(2, 2), (0, 1), (2, 2), (0, 2), (2, 2)]



