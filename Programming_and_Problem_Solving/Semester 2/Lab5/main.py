# ScriptName: main.py
# Author: Ronan Mullins 121107333

from my_functions import *

def main():
    """
    Call the functions defined in the functions.py file
    """
    print(read_file("P AND PS/Programming_Folder/SEMESTER 2/Lab5/tv_shows.txt"))
    write_dict(read_file("P AND PS/Programming_Folder/SEMESTER 2/Lab5/tv_shows.txt"), "output.txt")


if __name__ == "__main__":
    ''' call the main() function in this file '''
    main()
