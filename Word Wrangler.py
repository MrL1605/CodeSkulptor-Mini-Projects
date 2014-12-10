#http://www.codeskulptor.org/#user36_8un66m2P7xQR7Ce.py

"""
Student code for Word Wrangler game
"""

import urllib2
import codeskulptor
import poc_wrangler_provided as provided

codeskulptor.set_timeout(10)
WORDFILE = "assets_scrabble_words3.txt"

# Functions to manipulate ordered word lists

def remove_duplicates(list1):
    """
    Eliminate duplicates in a sorted list.

    Returns a new sorted list with the same elements in list1, but
    with no duplicates.

    This function can be iterative.
    """    
    _dum_list1=list(list1)
    _dum_i=0
    #to check if duplicate found         
    flag=0
    if (len(_dum_list1)==1 or len(_dum_list1)==0):
        return list1
    for _dum_i in range(3):
        _dum_i=0
        flag=0
        while _dum_i<len(_dum_list1)-1:
            #so that not whole of list is searched again
            if (flag==0):
                _dum_j = _dum_i + 1
            #Recheck that postion if a element is repeated
            else:
                _dum_i -=1
                _dum_j = _dum_i+1
                flag=0
            #Every element in list1 is checked,if found break
            while _dum_j<len(_dum_list1):
                if (_dum_list1[_dum_i] == _dum_list1[_dum_j]):
                    flag=1
                    break
                _dum_j+=1
            #If found shift every element forward by one postion 
            #and pop out the last position
            if (flag==1):    
                while _dum_j<len(_dum_list1)-1:
                    _dum_list1[_dum_j] = _dum_list1[_dum_j+1]
                    _dum_j+=1
                _dum_list1.pop(-1)
            _dum_i+=1
    return _dum_list1

def intersect(list1, list2):
    """
    Compute the intersection of two sorted lists.

    Returns a new sorted list containing only elements that are in
    both list1 and list2.

    This function can be iterative.
    """
    if list1==[] or list2==[]:
        return []
    list3=[]
    _dum_i=0
    _dum_j=0
    while _dum_i < len(list1) and _dum_j < len(list2): 
        if (list1[_dum_i]<list2[_dum_j]):
            _dum_i+=1
        elif (list1[_dum_i]>list2[_dum_j]):
            _dum_j+=1
        elif (list1[_dum_i]==list2[_dum_j]):
            list3.append(list1[_dum_i])
            _dum_i+=1
            _dum_j+=1
    return list3

# Functions to perform merge sort

def merge(list1, list2):
    """
    Merge two sorted lists.

    Returns a new sorted list containing all of the elements that
    are in either list1 and list2.

    This function can be iterative.
    """   
    if list1==[]:
        return list2
    elif list2==[]:
        return list1
    list3=[]
    for _dum in range(len(list1)+len(list2)):
        list3.append(0)
    _dum_i=0
    _dum_j=0
    _dum_k=0
    while _dum_i<len(list1) and _dum_j<len(list2):
        if (list1[_dum_i]<list2[_dum_j]):
            list3[_dum_k]=list1[_dum_i]
            _dum_i+=1
        else :
            list3[_dum_k]=list2[_dum_j]
            _dum_j+=1
        _dum_k+=1
    if _dum_i==(len(list1)):
        while _dum_j<len(list2):
            list3[_dum_k]=list2[_dum_j]
            _dum_j+=1
            _dum_k+=1
    else :
        while _dum_i<len(list1):
            list3[_dum_k]=list1[_dum_i]
            _dum_i+=1
            _dum_k+=1
    return list3

def merge_sort(list1):
    """
    Sort the elements of list1.

    Return a new sorted list with the same elements as list1.

    This function should be recursive.
    """
    low = 0
    high = len(list1)-1
    mid = int((low+high)/2)
    list0=list1
    if (low<high):
        list8 = merge_sort (list1[:mid+1] )
        list9 = merge_sort (list1[mid+1:] )
        list0 = merge (list8, list9 )
    return list0

# Function to generate all strings for the word wrangler game

def gen_all_strings(word):
    """
    Generate all strings that can be composed from the letters in word
    in any order.

    Returns a list of all strings that can be formed from the letters
    in word.

    This function should be recursive.
    """
    if len(word)<1:
        list1=['']
        return list1
    else :
#        
#        ** Algorithm **
#        make a new list that is empty
#        for every string in rest_strings
#            do the following in a loop
#                concatenate first to the beginning of the string add that new string to the new list
#                slice the string at position 1 
#                concatenate the left slice to first then concatenate the right slice
#                slice the string at position 2 
#                concatenate the left slice to first then concatenate the right slice
#                keep doing this until you concatenate first to the end of the string
#        now combine rest_strings and the new list into one list and return it
#        
        line0 = []
        first = word[0]
        rest_strings = gen_all_strings(word[1:])
        for string in rest_strings:
            if string != '':
                pos=0
                while pos<=len(string):
                    new_word=string[:pos]+first+string[pos:]
                    line0.append(new_word)
                    pos+=1
            else:
                line0.append(first)
        return rest_strings+line0

# Function to load words from a file

def load_words(filename):
    """
    Load word list from the file named filename.

    Returns a list of strings.
    """
#    url_file = codeskulptor.file2url(filename)
#    net_file = urllib2.urlopen(url_file )
    
#    words_grid=[]
#    for line in net_file.readlines():
#        letter = 0
#        curr_word = ''
#        for letter in range(len(line)):
#            curr_word = curr_word + line[letter]
#        words_grid.append(curr_word)
#        curr_word = ''
    return []

def run():
    """
    Run game.
    """
    words = load_words(WORDFILE)
    wrangler = provided.WordWrangler(words, remove_duplicates, 
                                     intersect, merge_sort, 
                                     gen_all_strings)
    provided.run_game(wrangler)

# Uncomment when you are ready to try the game
#run()
#import user36_Yqz4xpLLQ9GHulY as testsuite
#
#testsuite.run_test1(remove_duplicates)
#testsuite.run_test2(intersect)
#testsuite.run_test3(merge)
#testsuite.run_test4(merge_sort)
#testsuite.run_all(remove_duplicates, intersect, merge, merge_sort)
    
#import user36_UCQdx0ysZUFYetB as testsuite
#
#testsuite.run_test1(remove_duplicates)
##testsuite.run_test2(intersect)
##testsuite.run_test3(merge)
##testsuite.run_test4(merge_sort)
#testsuite.run_test5(gen_all_strings)
#testsuite.run_all(remove_duplicates, intersect, merge, merge_sort, gen_all_strings)    
    

