# ScriptName: my_functions.py
# Author: Ronan Mullins 121107333
# template for calling functions in another file

from logging import error


def to_english(n:int)->str:
    '''
    A function which takes in a integer value n and returns that integer in written english.
    it is assumed that n is an integer between the values -999 and 999
    '''
    try:
        if type(n) != int: #if n isn't an int, raise an error
            raise error
        if n <= -1000 or n >= 1000: #make sure number is between -999 and 999
            raise error

        num_in_words = "" #empty str

        d = {0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten',
            11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen', 
            
            20: 'twenty', 30: 'thirty', 40: 'forty', 50: 'fifty', 60: 'sixty', 70: 'seventy', 80: 'eighty',
            90: 'ninety', 
            
            100: 'one hundred', 200: 'two hundred', 300: 'three hundred', 400: 'four hundred', 
            500: 'five hundred', 600: 'six hundred', 700: 'seven hundred', 800: 'eight hundred', 900: 'nine hundred'
            
            } #construct the dictionary containing 0-19, the tens and the hundreds.

        if n in d: #if in the dictionary, just set the variable to the str in the dictionary

            num_in_words = d[n]
            return num_in_words.capitalize() #return capitalised str

        if n < 0: #negative

            if n < 0 and n > -9 : #if between n is between 0 and 9, single digit
                
                num_in_words = d[n*-1] #make the key positive in the key. single digit
                num_in_words = "minus " + num_in_words #add minus to front of string
        
            elif n <= -9 and n > -99: #if between -9 and -99, double digit

                n = n * -1 #make the key positive
                num_in_words = d[n-n%10] + " " + d[n%10] #find the ten and one of the number, concat into a str. double digit
                num_in_words = "minus " + num_in_words #add minus to front of string

            elif n <= -99 and n >= -999: #if between -99 and -999, triple digit
                n = n * -1 #make the key positive
                num_in_words = d[n-n%100] +" and "+ d[(n-n%10)-(n-n%100)] + " " + d[n%10] #find the hundred, ten and one of the number, concat into string. triple digit
                num_in_words = "minus " + num_in_words #add minus to front of string
        
        else: #positive

            if n <= 9: #if between n is between 0 and 9, single digit

                num_in_words = d[n] #find the one of the number, single digit
        
            elif n <= 99: #less than or equal 99, double digit

                num_in_words = d[n-n%10] + " " + d[n%10] #find the ten and one of the number, concat into a str. double digit

            elif n <= 999: #less than or equal 999, triple digit

                num_in_words = d[n-n%100] +" and "+ d[(n-n%10)-(n-n%100)] + " " + d[n%10] #find the hundred, ten and one of the number, concat into string. triple digit

        return num_in_words.capitalize() #return capitalised str

    except:

        return "Oops"




