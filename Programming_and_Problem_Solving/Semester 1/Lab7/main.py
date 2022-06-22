# ScriptName: main.py
# Author: Ronan Mullins 121107333

from my_functions import *


def main():
    """
    Call the functions defined in the functions.py file
    """
    
    #A #Fully Checked
    print(count([1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 3, 2, 1], 4))
    print(count([1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 3, 2, 1], 8))
    print(count("hello", "l"))
    print(count("hello", "h"))
    print(count("hello", "w"))
    print(count(234,23))
    print(count(True,True))
    print(count(234.2,23.2))
    print(count())

    #B #Fully Checked
    print(index("hello","o")) #y
    print(index("hello","z")) #y
    print(index("hello","r")) #y
    print(index(True,True)) #y
    print(index("h","hello")) #y
    print(index(True,"hello")) #y
    print(index("h",True)) #y
    print(index("h"))

    #C #Fully Checked
    print(get_value("hello",-6)) #h prob
    print(get_value("hello",4))
    print(get_value("hello",1))
    print(get_value(1,"hello")) #h prob
    print(get_value(-1,"hello")) #h prob
    print(get_value(100,"hello")) #h prob
    print(get_value("hello",True)) 
    print(get_value(True,"hello")) #h prob 
    print(get_value(True,True)) #h prob 
    print(get_value(1.0,2)) # h prob
    print(get_value("hello",2.0)) #h prob 
    print(get_value(1.0,2.2)) #h prob
    print(get_value(1,2))
    
    #D Fully Checked
    print(insert("hello", 5, "a"))
    print(insert("hello", 0, "a"))
    print(insert("hello", -6, "a"))
    print(insert("hello", 0.1, "a"))
    print(insert("hello", -6, "a"))
    print(insert("hello", "a"))
    print(insert())

    #E Fully Checked
    print(value_in_list("hello","e"))
    print(value_in_list(21,"e"))
    print(value_in_list("hello",21))
    print(value_in_list("hello","t"))
    print(value_in_list("hello",False))
    print(value_in_list(False,False))
    print(value_in_list("hello"))
    print(value_in_list())
    
    
    #F Fully Checked
    print(concat("hello"," there"))
    print(concat(True, False))
    print(concat([3],[1]))
    print(concat("hello"," there"))
    print(concat())

    #G Fully Checked
    print(remove(True, "hello"))
    print(remove("j", "hello"))
    print(remove())
    print(remove("h", "hello"))
    print(remove("e", "hello"))
    print(remove("l", "hello"))
    print(remove("l", "hello"))
    print(remove("o", "hello"))







if __name__ == "__main__":
    ''' call the main() function in this file '''
    main()
