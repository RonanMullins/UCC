# ScriptName: my_functions.py
# Author: Ronan Mullins 121107333

'''
PROBLEM STATEMENT

Take a random string containing random characters.
Format the str and remove the numbers from the string.
If a capital letter is present between two digits, increase the unicode left/right of the capital by 1 
If either left/right of a capital letter are not a digit, then don't do anything.
Remove duplicate digits in the sequence.
Calculate the sum of the numbers present in the sequence.
Calculate the sum of the numbers missing in the sequence.
Find the difference of these two sums.


- input must contain digits
- duplicate numbers must be removed

Assumptions:

The inputs are strings 
Floats will not be in the string

'''

from distutils.log import error
from logging import exception


def difference_of_numbers(characters:str) -> str:
    '''
    Function which takes in a str of characters. 
    Formats the string, increases ord unicode of digits either side of a capital letter by 1.
    Removes all letters.
    It calculates the sum of numbers present minus the sum of the numbers missing in the inputted sequence.
    It is assumed values inputted are strings.
    It returns a string.
    '''
    try:

        #error handling
        if characters == True or characters == False:
            raise Exception("Input must not be a boolean value!")
        if type(characters) != str:
            raise Exception("Input must be a str!")

        characters = characters.strip("\n") #remove returns
        characters = characters.strip() #remove blanks spaces either ends
        characters = characters.replace(" ","") #replace blank spaces with ""

        #increase ord unicode left/right of a single capital letter
        chars_list = list(characters)
        for char in range(0, len(chars_list)): #go through every char in the list

            if chars_list[char].isupper() and chars_list[char - 1].isdigit() and chars_list[char + 1].isdigit(): #is the char upper case? also left/right are digits?
                
                left_new_char = chr(ord(chars_list[char - 1]) + 1) # update the character by increasing ord() of the left character
                chars_list[char - 1] = left_new_char #assign the new character 

                right_new_char = chr(ord(chars_list[char + 1]) + 1) # update the character by increasing ord() of the right character
                chars_list[char + 1] = right_new_char #assign the new character 

        #list to str
        char_str = ""
        for char in chars_list: 
            char_str = char_str + str(char) #cycle through list and add values to a new str variable

        #declare empty strings and lists
        temp_string = "" 
        temp_list = [] 
        num_list = []
        for char in char_str: #go through every char in the str
            if char.isdigit(): #is it a digit?
                temp_string = temp_string + char #add the digit to a temp string
            else:
                temp_string = temp_string + " " #add this everytime there is no digit

        temp_list = temp_string.split(" ") #now make a new list by splitting where the blank spaces are

        for x in temp_list: #go through the temp list
            if x != '': #theres no empty space? then add to the num list
                x = int(x)
                num_list.append(x)
        
        #check there's digits present and the list isn't empty
        if not num_list:
            raise Exception("No numbers in the sequence!")
    
        num_list = list(dict.fromkeys(num_list)) #remove duplicate values
        num_list.sort() #sort numbers 
        min_num = int(num_list[0]) #set min number
        max_num = int(num_list[len(num_list)-1]) #set max number
        missing_sum = 0 #set sum of missing numbers to 0
        present_sum = 0 #set sum of present numbers to 0

        for x in range(min_num, max_num + 1): #go through from min to max numbers

            if x not in num_list: #if x isn't in the list then add it to the missing_sum tally
                missing_sum = missing_sum + x 
            else: # otherwise add to the present_sum tally
                present_sum = present_sum + x
                
        ret_val = present_sum - missing_sum #calculate the difference

        return "Difference of numbers = " + str(ret_val) # return :)

    except Exception as e:
        return "difference_of_numbers() Problem! " + str(e)
