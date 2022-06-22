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

    #Exercise 1  #checked
    
    print(seasons(1)) #winter
    print(seasons(2)) #spring
    print(seasons(3)) #summer
    print(seasons(4)) #autumn

    print(seasons(0))
    print(seasons(-1))
    print(seasons(5))
    print(seasons("a"))
    
    
    #Exercise 2  #checked

    print(slice_reverse(12321))# -> True (This is the boolean True and not the string "True") 
    print(slice_reverse( [1, 2, 3, 2, 1] ))# -> True
    print(slice_reverse("rotavator")) # -> True
    print(slice_reverse(("r","o","t","a","v","a","t","o","r"))) #-> True
    print(slice_reverse( " " ))# ->True (a string space)
    print(slice_reverse("abcdba"))# -> False
    print(slice_reverse("121"))

    #Exercise 3 #checked

    print(add_to_list(5, [1,2,"a",9]))# -> [1,3,5,7,9]
    print(add_to_list("c", ["a","b","d","e"])) #-> ["a","b","c","d","e"]
    print(add_to_list(5, [1,5,7,9])) #-> [1,5,7,9]
    
    print(add_to_list(5)) # -> [5]

    print(add_to_list(5, 5)) #-> “Incorrect value defined for param list”
    
    print(add_to_list(5, ["2","a","b","2"])) #-> “sort() does not like this mixture of elements”

    print(add_to_list(["streee"]))

    

    #Exercise 4

    print(add_to_list_no_sort (5, [9,3,7,9])) #-> [1,3,5,7,9]
    
    print(add_to_list_no_sort (5, [1,5,7,9])) #-> [1,5,7,9]
    print(add_to_list_no_sort (5)) #-> [5]

    

    print(add_to_list_no_sort (5, 5)) #-> “Incorrect value defined for param list”

    #print(add_to_list_no_sort ("a", [9,9,9,1]))

    print(add_to_list_no_sort ("a", ["e","d","c","b"]))

    print(add_to_list_no_sort ("g", ["b","a","d","e"])) 

    print(add_to_list_no_sort (8, ["a","g","d","e"])) #-> [5, "a","b","c","d"]
    

if __name__ == "__main__":
    ''' call the main() function in this file '''
    main()
