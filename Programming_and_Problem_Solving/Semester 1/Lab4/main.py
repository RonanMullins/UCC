# ScriptName: main.py
# Author: Ronan Mullins 121107333

# template for calling functions in another file

# import my_functions from other files - different options
# from my_functions import print_function
# import my_functions - when you use this you need to call the function using 'my_functions.<function_name>'
# this option imports all my_functions, using '*'

from my_functions import *


def main():
    """
    Call the functions defined in the functions.py file
    """

    
    ###E1### all cases checked

    # seperated_input("phineas", "ferb", " and ", " rock!!!\n")
    # seperated_input("doofenshmirtz", "incorporated", " Evil ", "!!!\n")
    # seperated_input("phineas", "ferb")
    # seperated_input(sepr="phineas", param2="ferb", endr=" and ", param1="rock!!!\n")
    # seperated_input("phineas", "ferb", "_", "_rock!!!\n")
    # seperated_input(1,2.0," and "," is three")


    ###E2### all cases checked

    # print(three_numbers(3,3,3))
    # print(three_numbers(3,3,3.1))
    # print(three_numbers(3,"&",3.3))
    # print(three_numbers("a","&","b"))


    ###E3### all cases checked

    # print(seasons(1))
    # print(seasons(2))
    # print(seasons(3))
    # print(seasons(4))
    # print(seasons(-1))
    # print(seasons(9999))
    # print(seasons("_"+"w"))
    # print(seasons("a"))


    ###E4### all cases checked 

    # print(grades(86))
    # print(grades(100))
    # print(grades(101))
    # print(grades(70))
    # print(grades("dog"))
    # print(grades(10000000000))
    

    ###E5### all cases checked

    # print(equal_numbers(25,25))
    # print(equal_numbers(5,3))
    # print(equal_numbers("a","a"))
    # print(equal_numbers(1,25))
    # print(equal_numbers(5,33))
    


if __name__ == "__main__":
    ''' call the main() function in this file '''
    main()

