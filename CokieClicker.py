#http://www.codeskulptor.org/#user34_SoXkU9OCcN_16.py

"""
Cookie Clicker Simulator
"""

import simpleplot
import math

# Used to increase the timeout, if necessary
import codeskulptor
codeskulptor.set_timeout(20)

import poc_clicker_provided as provided

# Constants
SIM_TIME = 10000000000.0

class ClickerState:
    """
    Simple class to keep track of the game state.
    """
    
    def __init__(self):
        self._total_cookies=0.0
        self._current_cookies=0.0
        self._current_time=0.0
        self._cps=1.0
        self._history=[(0.0, None, 0.0, 0.0)]
        
    def __str__(self):
        """
        Return human readable state
        """
        return "\ncurrent_cookies"+str(self._current_cookies)+"\ntotal_cookies"+str(self._total_cookies)+"\ncur_time"+str(self._current_time)+"\ncps"+str(self._cps)
        
    def get_cookies(self):
        """
        Return current number of cookies 
        (not total number of cookies)
        
        Should return a float
        """
        return self._current_cookies
    
    def get_cps(self):
        """
        Get current CPS

        Should return a float
        """
        return self._cps
    
    def get_time(self):
        """
        Get current time

        Should return a float
        """
        return self._current_time
    
    def get_history(self):
        """
        Return history list

        History list should be a list of tuples of the form:
        (time, item, cost of item, total cookies)

        For example: (0.0, None, 0.0, 0.0)
        """
        return self._history

    def time_until(self, cookies):
        """
        Return time until you have the given number of cookies
        (could be 0 if you already have enough cookies)

        Should return a float with no fractional part
        """
        if cookies < self.get_cookies():
            return 0.0
        else:
            return math.ceil((cookies - self.get_cookies()) / self.get_cps())
    
    def wait(self, time):
        """
        Wait for given amount of time and update state

        Should do nothing if time <= 0
        """
        if (time<=0):
            return
        self._current_time += time
        self._current_cookies += self._cps * time
        self._total_cookies += self._cps * time
    
    def buy_item(self, item_name, cost, additional_cps):
        """
        Buy an item and update state

        Should do nothing if you cannot afford the item
        """
        if (self._current_cookies>=cost):#
            self._current_cookies-=cost
            self._cps+=additional_cps
            self._history.append(( self._current_time , item_name , cost , self._total_cookies))
    
def simulate_clicker(build_info, duration, strategy):
    """
    Function to run a Cookie Clicker game for the given
    duration with the given strategy.  Returns a ClickerState
    object corresponding to game.
    """
    cookie_obj=ClickerState()
    clone_obj=build_info.clone()    
    while ( cookie_obj.get_time() <= duration ):
        time_left = duration - cookie_obj.get_time()
        if (cookie_obj.get_cookies() > clone_obj.get_cost("Cursor")):
            buy_item=strategy( cookie_obj.get_cookies() , cookie_obj.get_cps() , time_left , clone_obj )
        else:
            buy_item=None
        if (buy_item == None):
            cookie_obj.wait( 1 )
            break
        else:
            time_requried = cookie_obj.time_until( clone_obj.get_cost( buy_item ))
            if ( time_left > time_requried ):
                cookie_obj.wait( time_requried )
            else :
                break
            cookie_obj.buy_item ( buy_item, clone_obj.get_cost(buy_item), clone_obj.get_cps(buy_item) )
            clone_obj.update_item( buy_item )        
    print cookie_obj.get_cookies()
    time_left=duration-cookie_obj.get_time()    
    if ( time_left <= duration ):  
        buy_item="Cursor"
        while ( cookie_obj.get_cookies() >= clone_obj.get_cost ( buy_item )):
            cookie_obj.buy_item ( buy_item, clone_obj.get_cost(buy_item), clone_obj.get_cps(buy_item) )
        cookie_obj.wait( time_left )        
    cookie_obj.__str__()
    return cookie_obj

def strategy_cursor(cookies, cps, time_left, build_info):
    """
    Always pick Cursor!

    Note that this simplistic strategy does not properly check whether
    it can actually buy a Cursor in the time left.  Your strategy
    functions must do this and return None rather than an item you
    can't buy in the time left.
    """    
    return "Cursor"

def strategy_none(cookies, cps, time_left, build_info):
    """
    Always return None

    This is a pointless strategy that you can use to help debug
    your simulate_clicker function.
    """
    return None

def strategy_cheap(cookies, cps, time_left, build_info):
    item_list=build_info.build_items()
    for _dummy_item in item_list:
        if (cookies >= build_info.get_cost( _dummy_item )):
            return _dummy_item
    return None

def strategy_expensive(cookies, cps, time_left, build_info):
    list_cost_item=[]
    item_list=build_info.build_items()
    for _dummy_item in item_list:
        list_cost_item.append(build_info.get_cost( _dummy_item ))
    max_cost_item=max(list_cost_item)
    if (cookies> max_cost_item or max_cost_item ==0):
        for _dummy in range(len(list_cost_item)):
            if (max_cost_item == list_cost_item[_dummy]):
                return item_list[_dummy]
    return None


def strategy_best(cookies, cps, time_left, build_info):
    buy_item=None
    if (cps<1.5):
        buy_item="Cursor"
    elif (cps>1.5 and cps<4):
        buy_item="Grandma"
    elif (cps>4 and cps<20):
        buy_item="Farm"
    elif (cps>20 and cps<60):
        buy_item="Factory"
    elif (cps>60 and cps<220):
        buy_item="Mine"
    elif (cps>220 and cps<620):
        buy_item="Shipment"    
    elif (cps>620 and cps<2220):
        buy_item="Alchemy Lab"    
    elif (cps>2220 and cps<22218):
        buy_item="Portal"    
    elif (cps>22218 and cps<219748):
        buy_item="Time Machine"
    elif (cps>219748 and cps<439496):
        buy_item="Antimatter Condenser"
    if (cookies > build_info.get_cost(buy_item)):
        return buy_item  
    return None

def run_strategy(strategy_name, time, strategy):
    """
    Run a simulation with one strategy
    """
    state = simulate_clicker(provided.BuildInfo(), time, strategy)
    print strategy_name, ":", state

    # Plot total cookies over time

    # Uncomment out the lines below to see a plot of total cookies vs. time
    # Be sure to allow popups, if you do want to see it

    history = state.get_history()
    history = [(item[0], item[3]) for item in history]
    simpleplot.plot_lines(strategy_name, 1000, 400, 'Time', 'Total Cookies', [history], True)

def run():
    """
    Run the simulator.
    """    
    run_strategy("best", SIM_TIME, strategy_best)

    # Add calls to run_strategy to run additional strategies
    # run_strategy("Cheap", SIM_TIME, strategy_cheap)
    # run_strategy("Expensive", SIM_TIME, strategy_expensive)
    # run_strategy("Best", SIM_TIME, strategy_best)
    

#run()
# testing __init__ , __str__, get_cookies, get_cps, get_time, get_history:    
#import user34_1yyodNweJj_0 as init_test
#init_test.run_test(ClickerState)
#
# testing wait
#import user34_gwOBYcB0vg_5 as wait_test
#wait_test.run_test(ClickerState)
#
# testing until
#import user34_JegqHUeyeq_1 as time_until_test
#time_until_test.run_test(ClickerState)
# testing buy_item: 
#import user34_CX25TCXsrD_6 as buy_test
#buy_test.run_test(ClickerState)



#Phase 2
#import user34_muNP84fR8e_2 as testsuite
#testsuite.run_tests(ClickerState,simulate_clicker,strategy_cursor)


#Phase 3
#import user34_muNP84fR8e_2 as testsuite
#testsuite.run_tests(ClickerState,simulate_clicker,strategy_cursor, 
#                    strategy_cheap, strategy_expensive, strategy_best)

#current_cookies5911771557.71
#total_cookies152255425036.0
#cur_time10000000000.0
#cps16.0
#
#Time: 10000000000.0
#Current Cookies: 6965195661.5
#CPS: 16.1
#Total Cookies: 153308849166.0


