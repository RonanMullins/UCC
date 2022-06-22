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
    
    print(to_english(142))
    print(to_english(-142))
    print(to_english(11))
    print(to_english(42))
    print(to_english(9))
    print(to_english(999))

    print(to_english(True))
    print(to_english([2]))
    
    print(to_english(999))
    

if __name__ == "__main__":
    ''' call the main() function in this file '''
    main()
