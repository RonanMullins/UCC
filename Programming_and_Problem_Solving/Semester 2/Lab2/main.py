# ScriptName: main.py
# Author: Ronan Mullins 121107333

from xml.etree.ElementTree import QName
from my_functions import *


def main():
    """
    Call the functions defined in the functions.py file
    """

    #Q1

    # print(times_tables(5,12))

    #Q2

    # print(getset([1,2,3,4,4]))

    #Q3

    # print(all_even([1,2,3,4])) #ret true
    # print(all_even([4,3,2,1])) #ret false
    # print(all_even([1,2,4,3])) #ret false

    #Q4

    # print(checkAllEven([1,2,3,4]))
    # print(checkAllEven([2,2,2,4]))

    #Q5

    # print(in_order(3,2,3))

    #Q6

    print(create_diction([1,2,3,4,2,3,4],[10, 20, 30, 40, 21, 31, 41]))   
    print(create_diction([1,2,3],[10, 20, 30, 40, 21, 31, 41]))   
    print(create_diction([1,"sssssss",3,4,2,3,4],[10, 20, 30, 40, 21, 31, 41]))  
    print(create_diction([1,2,3,4,2,3,4],[10, 20, True, 40.4444, 21, 31, 41])) 







if __name__ == "__main__":
    ''' call the main() function in this file '''
    main()
