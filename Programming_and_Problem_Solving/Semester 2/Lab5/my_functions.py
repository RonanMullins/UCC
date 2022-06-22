# ScriptName: my_functions.py
# Author: Ronan Mullins 121107333

def read_file ( input_file: str )-> dict:
    '''
    A function which takes in a file, opens the file and then reads through it line by line to extract the data. this data is then formatted and returned as a dictionary 
    it is assumed that the file may contain duplicate entries
    it is assumed the file may have blank gaps and returns
    it is assumed that in the file, each show_id will only have 2 values. if there is a duplicate of the show_id this function will append the values to the initial key
    '''
    try:

        in_file = open(input_file, "r")

        return_dictionary = {}

        for line in in_file: #for every line in the file

            if line == "\n": #if one line is empty just continue the moving through the file
                continue
            else:
                line = line.strip("\n") #remove returns
                line = line.strip() #remove blanks spaces either ends
                line = line[1:-1] #remove characters either ends "{" and "}" in this case
                line = line.replace(",",":") #replace , with :
                content = line.split(":") #splits into a list of strings at : as a separator  
                key = int(content[0].strip()) #select at position 0 and remove blank spaces either end
                char_name = content[1].strip().strip("\"")#select at position 0. remove blank spaces either end and quotation marks
                char_address = content[2].strip().strip("\"")#select at position 0.remove blank spaces either end and quotation marks
                            
                if key in return_dictionary.keys(): #if the key exists already
                    return_dictionary[key].append([char_name, char_address]) #append the values to that key
                else:
                    return_dictionary[key] = [[char_name, char_address]]  #else we proceed as normal by assigning values to a key
                
        in_file.close() #close file
        return return_dictionary 
        
    except Exception as e:
        return "Oops " + str(e)
        



def write_dict(d:dict, output_file:str)-> str:
    '''
    A function which takes in d (a dictionary) and an output_file (a file). the function takes the data in the dictionary and writes it to that file.
    it's assumed that d is a dictionary and out_file is a file.
    '''
    try:
        out_file = open(output_file, "w") #open file to write to
        
        for key, value in d.items(): #for key and value in the items of the dictionary
            for i in range(len(value)): #for i in the range of the length of the value

                out_file.write("id " + str(key) + "\thas (a character/characters) " + value[i][0] + " with (an address/addresses) of " + value[i][1] + "\n") #formatted string

                #value[i][0] is the character's name, value[i][1] is the character's address. i is a set of char name and char address within the value tuple of the dictionary.

        out_file.close()#close the file
    
    except Exception as e:
        return "Oops " + str(e)



