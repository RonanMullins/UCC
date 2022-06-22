# ScriptName: my_functions.py
# Author: Ronan Mullins 121107333

from logging import error
from xmlrpc.client import boolean

#question 1
def times_tables(num1:int, num2:int)->str:
    '''
    Function that takes in two ints and returns the times tables of num1 up to num2
    '''
    try:

        i=1 #set i to 1
        s=""#create an empty string

        while i <= num2: #while i is less than num2

            sum = num1*i #sum is i multiplied by num1
            line=str(num1)+" X "+str(i)+" = "+str(sum)+"\n" #this is the format of each "line"
            s = s + str(line) #add the line to the empty string
            i+=1 #iterate i

        return s #return the string
    
    except:

        return "Oops"
#question 2
def getset(inputList: list)->list:
    '''
    A function which takes in a list and returns the unique values in the list
    '''
    try:
        unique = [] #make empty list called unique
        x=0 #let x equal zero
    
        while x < len(inputList): #while x is less than the length of the inputList

            if inputList[x] not in unique: #if the inputList at x is not in the unique list the append
            
                unique.append(inputList[x])
            x+=1 #increment x

        return unique #return the finished list
    except:

        return "Oops"
#question 3
def all_even(a_list:list)->bool:
    '''
    A function which takes in a list and returns a boolean true or false depending whether the list is in ascending or descending order

    Ascending - True
    Descending - False
    '''
    try:

        i=1 #let i equal 1

        while i < len(a_list): #while i is less than the length of a_list

            if a_list[i]<a_list[i-1]: #if the value at position i is less than the value at i-1 then return false

                return False

            i+=1 #increment i

        return True #passed through the whole list without returning false, so then return True
    except:

        return "Oops"
#question 4
def checkAllEven(lst: list)->bool:
    '''
    Function which takes in a list and returns a boolean depending if the contents of the list are odd/even

    even list - True 
    odd in the list - False
    '''
    try:

        for x in range(len(lst)): #for x in the length of lst

            if lst[x]%2==0: #check if even using modulus 2

                continue #continue code if even

            else:

                return False #return a false if there is an odd value

        return True #true if false isnt returned
    except:

        return "Oops"
#question 5
def in_order(a:int,b:int,c:int)->str:
    '''
    Function which takes in three integers and returns the message "all numbers in order". if not in order return "not in order"
    '''
    try:

        if(a<b): #a is less than b
            if(b<c): #b is less than c
                if(c>b):  #c is less than b
                    return "all numbers in order" #must be in order, return the message

        else:
            return "not in order" #failed the checks, return the message
    except:

        return "Oops"
#question 6
def create_diction(list_of_keys: list, list_of_values:list)->dict:
    '''
    Function which takes in two lists and merges them into a dictionary
    '''
    try:
        d = {} #define the dictionary

        if len(list_of_keys)!=len(list_of_values):

            raise error

        for i in range(len(list_of_keys)): 
        
            if list_of_keys[i] in d.keys(): #if value at i is a key in d that already exists

                d[list_of_keys[i]].append(list_of_values[i]) #append to dict

            else: #make a new key, the key doesnt exist in the dictionary

                d[list_of_keys[i]] = [list_of_values[i]] #create the key and set the value

        return d #return finished dict

    except:

        return "Oops"




