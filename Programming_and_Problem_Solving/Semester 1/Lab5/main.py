# ScriptName: main.py
# Author: Ronan Mullins 121107333

# template for calling functions in another file

# import my_functions from other files - different options
# from my_functions import print_function
# import my_functions - when you use this you need to call the function using 'my_functions.<function_name>'
# this option imports all my_functions, using '*'
from my_functions import *


def main():
    
    

    #Exercise 1

    # print(fizz_buzz(3))
    # print(fizz_buzz(5))
    # print(fizz_buzz(15))
    # print(fizz_buzz(15,3,5))
    # print(fizz_buzz('a'))
    # print(fizz_buzz(-15))


    #Exercise 2

    # print(fizz_buzz(3))
    # print(fizz_buzz(5))
    # print(fizz_buzz(15))
    # print(fizz_buzz(14))
    # print(fizz_buzz('a'))
    # print(fizz_buzz(-15))
    # print(fizz_buzz(3))
    # print(fizz_buzz(5))
    # print(fizz_buzz(15)) 
    # print(fizz_buzz(14))
    # print(fizz_buzz('a')) 
    # print(fizz_buzz(4, 4, 6))
    # print(fizz_buzz(6, 4, 6)) 
    # print(fizz_buzz(15, 3, 5))

    # print(fizz_buzz(0))
    #print(fizz_buzz(0,0,0))
    #print(fizz_buzz(0,1,1)) #num1 can be zero
    #print(fizz_buzz(1,0,1)) #d1 cant be zero
    #print(fizz_buzz(1,1,0)) #d2 cant be zero
    #check for zero use q4 for that

    
    #Exercise 3 #checked

    # print(grades(86))
    # print(grades("A"))
    # print(grades("B"))
    # print(grades("C"))
    # print(grades("D"))
    # print(grades("E"))
    # print(grades("F"))

    # print(grades(110))
    # print(grades("H"))
    # print(grades("a"))
    # print(grades("      a"))

    # print(grades(-11))
    # print(grades(True))
    # print(grades("a"))
    # print(grades("b"))
    # print(grades(0))

    #Exercise 4 

    print(fizz_buzz(3)) #fizz
    print(fizz_buzz(5)) #buzz
    print(fizz_buzz(15)) #fizzbuzz
    print(fizz_buzz(14)) #14
    print(fizz_buzz('a')) #input value(s) must be a number
    print(fizz_buzz(4, 4, 6)) #fizz
    print(fizz_buzz(6, 4, 6)) #buzz
    print(fizz_buzz(15, 3, 5)) #fizzbuzz

    print(fizz_buzz(1,'a','a'))
    print(fizz_buzz('a',1,'a'))
    print(fizz_buzz('a','a',1)) #work 
    print(fizz_buzz('a','a','a'))
    
    print(fizz_buzz('a')) #works

    print(fizz_buzz(0))
    print(fizz_buzz(0,0,0))

    print(fizz_buzz(-15))
    print(fizz_buzz(-15, -4, -1))


if __name__ == "__main__":

    main()


#param:str #hint