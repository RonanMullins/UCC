# ScriptName: my_functions.py
# Author: Ronan Mullins 121107333

# template for calling functions in another file
# def print_function():
#     print("I'm in another file :)")

import math

#################################
          #Exercise 1
#################################

def seperated_input(param1,param2,sepr=" ",endr="\n"):

    param1_str=str(param1)
    param1_cap=param1_str.capitalize() #capitalize parameters

    param2_str=str(param2)
    param2_cap=param2_str.capitalize()
    
    return print(param1_cap, param2_cap, sep=sepr, end=endr)

      
#################################
          #Exercise 2
#################################

def three_numbers(number_1,number_2,number_3):
    
    if(type(number_1) == int or type(number_2) == int or type(number_3) == int): #is it an int?

        if(number_1==number_2 and number_1==number_3 and number_2==number_3):

            #print("True")   

            return True

        else:

            #print("False")
            
            return False

    
    if(type(number_1) == float or type(number_2) == float or type(number_3) == float): #is it a float?

        if(number_1==number_2 and number_1==number_3 and number_2==number_3):

            #print("True")   

            return True

        else:

            #print("False")
            
            return False

    
    if(number_1 != int or number_2 != int or number_3 != int): #is it not an int?
        
        #print("False")
        
        return False
    
    if(number_1 != float or number_2 != float or number_3 != float): #is it not a float?
        
        #print("False")

        return False


    
#################################
          #Exercise 3
#################################

def seasons(number):

    if(type(number)==int):

        if(number<=0):
            
            return "Number entered, "+str(number)+", is outside of input values"

        if(number==1):
            
            return "Winter"

        if(number==2):
            
            return "Spring"

        if(number==3):
            
            return "Summer"

        if(number==4):
            
            return "Autumn"

        if(number>=5):

            return "Number entered, "+str(number)+", is outside of input values"

    else:

        return "Input value must be a number"


#################################
          #Exercise 4
#################################

def grades(grade):

    

    if(type(grade)!= int and type(grade)!= float): #check if input is not an int and not a float

        return "Input value must be a number"

    else:
        
        if(grade<0 or grade>100): #is it out of range? return "X"

            return "X"

        else: #what grade is it?

            if(grade>=0 and grade<=24):

                return "F"

            if(grade>=25 and grade<=39):

                return "E"

            if(grade>=40 and grade<=54):

                return "D"

            if(grade>=55 and grade<=69):

                return "C"

            if(grade>=70 and grade<=84):

                return "B"

            if(grade>=85 and grade<=100):

                return "A"


#################################
          #Exercise 5
#################################

def equal_numbers(number_1,number_2):

    if(type(number_1) != int or type(number_2) != int ):

        return "Input value(s) must be a number"
    
    
    else:

        if(number_1==number_2):

            return float(math.sqrt(number_1)) #return sqrt of number_1

        else:

            s_number_1= int(number_1**2) 
            s_number_2= int(number_2**2)

            return "("+str(s_number_1)+", "+str(s_number_2)+")" #returns squares of both numbers




    
    
