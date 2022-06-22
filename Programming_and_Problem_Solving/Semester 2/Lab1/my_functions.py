# ScriptName: my_functions.py
# Author: Ronan Mullins 121107333

#add hints,comments and docstrings

#exercise 1

from distutils.log import error
from logging import raiseExceptions


def firsts(s:str) -> str:
    '''
    Takes in str input, outputs the first occurences of each character in that str
    '''
    try:

        firsts_str= "" #lets make an empty str for the sorted characters
        s=str(s) #cast the input to a str
        for x in s:

            if x not in firsts_str:
                firsts_str = firsts_str + x #if not in s then add it to the firsts str

        return firsts_str
    except:
        return "Oops"

#exercise 2
def F(s1: str, s2: str) -> str:
    '''
    takes in values and outputs the shared values between the two inputs
    '''
    try:

        r = [] #empty list
        e1 = 0 #set counters to 0
        e2 = 0

        while e1 < len(s1):#loop while e1< length of s1
            while e2 < len(s2):#loop while e2< length of s2
                if(s1[e1] == s2[e2]):#if theyre equal at index add s1[e1] to the list
                    r += s1[e1]
                    break
                e2 += 1 #increment
            e1 += 1 #increment
        return r #return the sorted list
    except:
        return "Oops"


#exercise 3
def iter_factorial(n:int) -> int:
    '''
    return factorial of a number
    '''
    try:
        
        facto = 0 #factorial set as 0 for now
        if n == 0: #return 1 if n is 0

            return 1

        if n < 0: #less than 0 is undefined, raise error

            raise error

        if n == 1: #return 1 if n is 1

            return 1

        while n > 0: #while n is greater than 0
            
            if n == 1: 
                return facto #return the number if the sequence hits 0 
            
            if facto > 0: #mulitply number by n minus 1 
                    facto = facto*(n-1)
            if facto == 0: #add n times n minus 1 to the factorial 
                    facto = facto + (n*(n-1))
                
            
            n -= 1 #decrement n
        return facto
    except:
        return "Oops"
   

#exercise 4
def removeVowels(sentence: str) -> str:
    '''
    this function removes vowels from a string.
    '''
    try:

        vowels = "aeiou" #vowels in a str
        filtered_list = [] #list for sorting
        l = 0 #count set to zero

        while l < len(sentence): #while the count is less than length of sentence, continue loop

            if sentence[l] not in vowels: #check sentence at l is not in vowels, add to list if this is the case
                filtered_list.append(sentence[l])
            l+=1 #increment
    
        return "".join(filtered_list) #return the list as a str

    except:

        return "Oops"


#exercise 5
def hailstone(n:int)->list:
    '''
    takes in n. operations (different cases if odd/even) are performed on n. the value converges to 1
    if n even, next value n/2
    if n odd, next value 3n+1

    sequence not stopping for some reason :(
    '''

    try:
        h_list = [] #hailstone list

        i = n #set the counter to inputted n
        h_list.append(n) #add this value to the hailstone list

        while i > 0: #while counter greater than 0 



            if n % 2 == 0: #if its even, perform operation and add to list

                n = int(n/2)
                h_list.append(n)

            if n % 2 != 0: #if its odd. perform operation and add to list

                n = int((3*n)+1)
                h_list.append(n)
            
            if n == 1: #if its 1, break

                break


            i -=1 #decremnet the counter

        return h_list #return the hailstone list



    except:
        return "Oops"


#exercise 6
def chooseLargest(a:list,b:list)->list:
    '''
    returns the largest values from two lists
    '''

    try:

        results = [] #list to store results
        i = 0 #counters set to 0
        j = 0

        while i < len(a): #loop while i is less than the length of a
            
            while j < len(b):#loop while j is less than the length of b
                results.append(max(a[i],b[j])) #add the max values to the new list
                i += 1 #increment counters
                j += 1
        return results #return the new list



    except:

        return "Oops"
    


#exercise 7
def loop_the_loop(a1:list,a2:list) -> list:
    '''Takes two lists and adds them together then adds it to a new list'''
    try:
        new_loop = [] #new loop list
        
        e1 = 0 #counters set to 0
        e2 = 0

        while e1 < len(a1): #while e1 is less than the length of a1. loop
            while e2 < len(a2): #while e2 is less than the length of a2. loop
                new_loop.append(a1[e1]+a2[e2]) #add to the list at these positions in a1 and a2
                e2 += 1 #increment
            e1 += 1 #increment
        return new_loop #return the new list
    except:
        return "Oops"



