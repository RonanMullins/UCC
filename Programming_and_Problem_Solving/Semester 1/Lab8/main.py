# ScriptName: main.py
# Author: Ronan Mullins 121107333

import random
from my_functions import *


def main():
    """
    Call the functions defined in the functions.py file
    """


    #Exercise 2  Fully checked

    # print(while_loop()) #-> [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    # print(while_loop(5)) #-> [1, 2, 3, 4, 5] (the list 1 to 5 is returned)
    # print(while_loop(-86)) #-> [1, 0, -1, -2 ,-3, -4 ,-5]
    
    # print(while_loop(5)) #-> [1, 2, 3, 4, 5, 15]
    # print(while_loop(14)) #-> [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 78]

    # print(while_loop("fffff"))
    # print(while_loop(True))





    #Exercise 3  Fully tested

    # print(magic_8_ball("is the sky blue?",[12,3,-1]))
    # print(magic_8_ball())
    # print(magic_8_ball("WEEEE"))
    # print(magic_8_ball(True))
    # print(magic_8_ball("can i fly?",[0,3,8,7])) #it is certain, yes definitley or yes
    #print(magic_8_ball([1],"rreee"))

    #Exercise 4 #Fully checked

    # print(all_pairs( [1,2], "abc" )) #-> (False, ["1a", "1b", "1c", "2a", "2b", "2c"])
    # print(all_pairs( [], "" )) #-> (False, [])
    # print(all_pairs( ["abc"], [1,2] )) #-> (False, ["abc1", "abc2"])
    # print(all_pairs( ["a","b"], "abc" )) #-> (False, ["aa", "ab", "ac", "ba", "bb", "bc"])
    # print(all_pairs( "", [] ))
    # print(all_pairs( [1,"b"], "abc" ))
    # print(all_pairs("12222","1"))
    # print(all_pairs( [], "" )) #-> (False, [])
    # print(all_pairs("",[])) #return false [] 
    # print(all_pairs([]))
    # print(all_pairs()) #return error true -1 

if __name__ == "__main__":
    ''' call the main() function in this file '''
    main()
