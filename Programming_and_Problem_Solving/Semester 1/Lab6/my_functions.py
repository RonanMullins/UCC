# ScriptName: my_functions.py
# Author: Ronan Mullins 121107333

'''
Exercise 1 

rewrite the seasons() from Lab 4.
Within this function, define a list of the seasons
select the season based on the input value where 1=Winter,2=Spring, 3=Summer, and 4=Autumn.

Remember list indexing begins at 0. All other error message handling, param names, etc., in the original function, must be kept.

'''
def seasons(number):
    '''
    take in a number
    line that number with the index of list

    '''
    seasons_list = ["Winter","Spring", "Summer", "Autumn" ] #define list
    
    
    if type(number)==int: #is input an int?

        new_num = number-1 #lines up number input with index


        if(new_num>=0 and new_num<4): #is the int in range?

            
            if(seasons_list[new_num]=="Winter"):
            
                return "Winter"

            if(seasons_list[new_num]=="Spring"):
            
                return "Spring"

            if(seasons_list[new_num]=="Summer"):
            
                return "Summer"

            if(seasons_list[new_num]=="Autumn"):
            
                return "Autumn"

        else:
            
            return "Number entered, "+str(number)+", is outside of input values"

    else:
        
        return "Input value must be a number"




'''
Exercise 2 

string slicing. Write a function, slice_reverse(input_value),

determine if the input_value is a palindrome

The program should return True or False (booleans) depending on then input. 

Do not use the Python reverse() function

'''

def slice_reverse(input_value):
    '''
    compared reversed string with the original str
    '''
    
    if type(input_value)==int: #if input is an int
        

        input_value_str=str(input_value)

        input_value_str_rev = input_value_str[::-1]

        if(input_value_str==input_value_str_rev):

            return True

        else:

            return False

    elif type(input_value == str or tuple or list):

        if(input_value==input_value[::-1]):

            return True
      
        else:
            return False




    

'''
Exercise 3

I want you to create a function called add_to_list(value, list)

return a sorted list. 

This function will add value to the list if the list does not already contain
the value.

For now, you can assume the list param is already sorted.

use the python function sort() to sort your returning list.

Sort() will not allow you to mix ints, floats and strings.

In your function set an appropriate default value for the list param.



'''

def add_to_list(value, list=[]):

    if not list: #if the list is empty, add value to the list

        
        list.append(value) #add the value 
        return list #return the list

        

    elif(type(list) == type([])): #if the list is list

        

        try:
            
            #if(type(value)==type(list[0])):

                if value in list:
                
                    return list

                elif value not in list:
                
                    list.append(value)
                    list.sort()
                    return list
                else:

                    raise Exception


        except Exception:
            
            return "sort() does not like this mixture of elements"
        

                
    else:

        
            
        return "Incorrect value defined for param list"

    
        
        
        

            
            

 





        

        
        
        
    




'''
Exercise 4

create a function called add_to_list_no_sort(value, list) which will return a sorted list. 

This function will add value to the list if the list does not already
contain the value.

For now, you can assume the list param is already sorted. 

In your function set an appropriate default value for the list param. 

In this function, you cannot use the python function “sort()” to sort your returning list. 

But you can now mix ints, floats and strings. If mixing ints, floats and strings, use ASCII values for
strings when comparing.

You can make 3 assumptions:

1. As we have not covered Loops in great detail, you can assume
the max length of list is 4 elements

2. The input list is already sorted

3. The input list consists of only type of value, i.e., all ints, all
string, etc.

'''


    
def add_to_list_no_sort(value,list=[]): 

    if not list: #if the list is empty, add value to the list

        
        list.append(value) #add the value 
        return list #return the list

        

    elif(type(list) == type([])): #if the list is list

        if value not in list:

            list.append(value) #add the value
            

            if(type(value) and type(list[0]))==(int or float): #if numerical
                
                i=0

                while i<10: #cycles through several times to finish sort

                    if(list[0]>list[1]):

                        list[0], list[1] = list[1], list[0] #multiple assignment to swap values

                    if(list[1]>list[2]):

                        list[1], list[2] = list[2], list[1]

                    if(list[2]>list[3]):

                        list[2], list[3] = list[3], list[2]

                    if(list[3]>list[4]):

                        list[3], list[4] = list[4], list[3]
                    i+=1

                return list
            
            
            else: #value and list must be different types
                
                i=0
            

                while i<10: #cycles through several times to finish sort

                    if(ord(str(list[0]))>ord(str(list[1]))):

                        list[0], list[1] = list[1], list[0]
                    
                    
                    if(ord(str(list[1]))>ord(str(list[2]))):

                        list[1], list[2] = list[2], list[1]

                    
                    if(ord(str(list[2]))>ord(str(list[3]))):

                        list[2], list[3] = list[3], list[2]

                    
                    if(ord(str(list[3]))>ord(str(list[4]))):

                        list[3], list[4] = list[4], list[3]


                    i+=1
                

                return list    
        else:

            return list
        
            
    else:
        
        return "Incorrect value defined for param list"

    
