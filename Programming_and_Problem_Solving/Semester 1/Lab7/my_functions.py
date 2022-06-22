# ScriptName: my_functions.py
# Author: Ronan Mullins 121107333


'''
a. count(my_list, value) - function to return the number of times value occurs in
my_list

i. count("hello", "l") -> 2 (the integer 2 is returned)

'''

def count(my_list =[], value=""):
    '''
    Function - count how many times <value> occurs in <my_list>
    :param list: - <my_list> input
    :param value: - <value> to search for
    :return: amount of times a value occurs
    '''
    try: #try this code

           
        i = 0  # set counter
        # accumulator to count how many times <value> occurs
        # set to zero to cover no <value> in <list>
        num_values = 0
        # loop over the length of the <list>
        while i < len(my_list):
            # if <value> and <list> index i are the same
            if my_list[i] == value:
                # increment the accumulator
                num_values += 1
            # increment the counter
            i += 1
        # return how many times <value> occurs in <list>
        return num_values
    
    except: #error? return this

        return "Houston, we have a problem!"



'''
b. index(my_list, value) - function to return the first index that value occurs in
my_list. Return -1 if the value does not occur in my_list

i. index("hello", "o") -> 4
ii. index("hello", "p") -> -1

'''

def index(my_list =[], value=""):
    '''
    Function - takes in a list and returns in the first index of the value
    :param list: - <my_list> input
    :param value: - <value> to search for index
    :return: index of the value in the list
    '''

    try: #try this code

        i=0 #define i, let it equal 0

        while i< len(my_list): #while i is less than the length of the list


            if(my_list[i]==value): #if the list at index i equals the value passed in 

                return i #return the index

            i+=1 #increment i
        else:

            return -1 #not in the list? return -1

    except: #error? return this

        return "Houston, we have a problem!"


'''
c. get_value(my_list, index) - function to return the value that occurs in my_list
at index

i. get_value("hello", 1) -> "e"

'''

def get_value(my_list =[], index=""):
    '''
    Function- take in a list and return the value at the given input.
    :param list: - <my_list> input
    :param index: - <index> to search for value
    :return: the value at an index in the list
    '''

    try: #try this code

        #if type(index) != bool: #if type is boolean then it would set 1 or 0 as the index. leaving this out as boolean returns a valid output

            return my_list[index] #return the value at index i 

    except: #error? return this

        return "Houston, we have a problem!"


'''
d. insert(my_list, index, value) - function to return my_list, after you have added
value at index (remember to check the length of my_list and if index is larger
than len(my_list) add as a new index at the end my_list)

i. insert("hello", 1, "a") -> "hallo"
ii. insert("hello", 5, "p") -> "hellop"

'''

def insert(my_list = [], index ="", value =""):
    '''
    Function take in a list and insert a given value at an index
    :param list: - <my_list> input
    :param index - <index> input
    :param value: - <value> to insert into list
    :return: insert the value at an index, add to end if index outside of index
    '''
    try: #try this code
        
        my_list1 = list(my_list) #cast to list
    

        if -1*len(my_list) <= index < len(my_list): #check if index is within the length of the list, including minus index

            my_list1[index] = value #let the list at the given index equal the value
            word = "" #define empty string 
            i = 0 #start index
        
            while i < len(my_list): #while i< length of the list
                word += my_list1[i] #add the value at i to the string 
                i += 1 #increment the index
            return word #return completed word

        else:

            word = "" #define empty string 
        
            i = 0 #start index
            while i < len(my_list): #while i< length of the list
                word += my_list1[i] #add the value at i to the string
                i += 1   #increment the index
            return word+value #return completed word and the value at end
           
    except: #error? return this

        return "Houston, we have a problem!"


'''
e. value_in_list(my_list, value) - function to return True or False if value occurs
in my_list

i. we can then use "if value_in_list(list, value):" as a boolean check
ii. value_in_list("hello", "o") - True
iii. value_in_list("hello", "a") - False

'''

def value_in_list(my_list =[], value =""):
    '''
    Function- take in a list and return a boolean True if value exists in the list, return a boolean False otherwise
    :param list: - <my_list> input
    :param value: - <value> value to check in list
    :return: True if value exists in the list, return a boolean False otherwise
    '''
 
    try: #try this code
        
        i=0 #define i, let it equal 0

        while i< len(my_list): #while i is less than the length of the list


            if(my_list[i]==value): #if the list at index i equals the value passed in

                return True #return boolean true

            i+=1 #increment i 
        else:

            return False #return boolean false
 

    except: #error? return this

        return "Houston, we have a problem!"


'''
f. concat(list1, list2) - function to return a new list, which is a combination of
list1 and list2

i. concat("hello", " world") -> "hello world"

'''
def concat(list1 =[], list2 =[]):
    '''
    Function- to return a new list, which is a combination of list1 and list2
    :param list1: - <my_list> input
    :param list2: - <my_list> input
    :return: concatenation of list1 and list2
    '''

    try: #try this code

        return list1+list2 #return concat list1 and list2

    except: #error? return this

        return "Houston, we have a problem!"


'''
g. remove(value, my_list) - function to return a list with the first occurrence of
value removed from my_list

i. remove("h", "hello") -> "ello"

'''

def remove(value="", my_list: list=[]):
    '''
    Function- return a list with the first occurrence of value removed from my_list
    :param value: - <value> value to remove
    :param list: - <my_list> the list to remove the value from
    :return: the list without the value   
    '''

    try: #try this code

        if(value in my_list): #does the value exist in the list?

            i=0 #let i equal 0 

            while i<len(my_list): #while i is less than the length of the list

                if(my_list[i]==value): #if we find the value

                    if(my_list[0]==value): #start of list?

                        return my_list[1:len(my_list)] #return the rest of list

                    else:

                        listleft = my_list[0:i] #make the left not including list at i
                        listright = my_list[i+1:len(my_list)] #make the right not including the list at i
                        return listleft+listright #return left and right
                i+=1 #increment the index

        else:
        
            raise Exception #the value isn't in the lists

    except: #error? return this

        return "Houston, we have a problem!"

