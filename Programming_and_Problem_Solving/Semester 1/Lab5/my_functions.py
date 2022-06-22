# ScriptName: my_functions.py
# Author: Ronan Mullins 121107333


'''
#Exercise 1

Pass a number, as parameter num1

For multiples of 3, return “Fizz”

For multiples of 5, return “Buzz” 

For numbers which are multiples of both 3 and 5 return “FizzBuzz” 

If none of the conditions are true, simply return the number itself

When the inputs are not integers, return the error statement 'Input value(s) must be a number’ 

'''

# def fizz_buzz(num1):   #EXERCISE 1 ORIGINAL


#     if(type(num1)==int):

#         if( num1%3==0 and num1%5==0 ): #both are multiples of 3 and 5

#             return "FizzBuzz"

#         elif( num1%3!=0 and num1%5!=0 ): #none are multiples of 3 and 5

#             return num1


#         elif(num1%3==0): #is num1 a multiple of 3

#             return "Fizz"

#         elif(num1%5==0): #is num1 a multiple of 5

#             return "Buzz"

#     else:

#         return "Input value(s) must be a number"


'''

#Exercise 2 

Rewrite the fizz_buzz() function. I want this functionality to remain in the new function
(remember default values).

Add two parameters, divisor_1 (parameter 2) and divisor_2 (parameter 3) x

For multiples of divisor_1 the function return “Fizz” 

For multiples of divisor_2, return “Buzz”

For numbers which are multiples of both divisor_1 and divisor_2 return “FizzBuzz”

'''


# def fizz_buzz(num1, divisor_1=3,divisor_2=5):

    

#     if(type(num1)==int):

#         if( num1%divisor_1 == 0 and num1%divisor_2 == 0 ): #both are multiples of 3 and 5

#             return "FizzBuzz"

#         elif( num1%divisor_1 != 0 and num1%divisor_2 != 0 ): #none are multiples of 3 and 5

#             return num1


#         elif(num1%divisor_1 == 0): #is num1 a multiple of 3

#             return "Fizz"

#         elif(num1%divisor_2 == 0): #is num1 a multiple of 5

#             return "Buzz"

#     else:

#         return "Input value(s) must be a number"





'''
#Exercise 3

Rewrite the grades() function from Lab 4,

adding a parameter called number.

In the original function, you passed a number to the function, which would
return the corresponding Letter Grade.

The function will now also take a Letter Grade and should return the Numerical Grade range

''' 
'''
    function takes in number parameter, checks if number is a str or int

    returns letter grade if int is given
    returns grade range if a letter between a-f is given

    for both cases it returns error message if value is out of range
'''

def grades(number):




        if(type(number)==int or type(number)==str):

            if(type(number)==int): #number an int?

                if(number<0 or number>100): #is it out of range?

                    return "The input numerical grade is outside the range supported"

                else: #what grade is it?

                    if(number>=0 and number<=24):

                        return "F"

                    if(number>=25 and number<=39):

                        return "E"

                    if(number>=40 and number<=54):

                        return "D"

                    if(number>=55 and number<=69):

                        return "C"

                    if(number>=70 and number<=84):

                        return "B"

                    if(number>=85 and number<=100):

                        return "A"
    
            elif(type(number)== str): #number a str?

                number_upper = number
                number_upper = number_upper.upper().strip() 
            
                if(number_upper == "A"):

                    return "85-100"
        
                elif(number_upper == "B"):

                    return "70-84"

                elif(number_upper == "C"):

                    return "55-69"

                elif(number_upper == "D"):

                    return "40-54"

                elif(number_upper == "E"):

                    return "25-39"

                elif(number_upper == "F"):

                    return "0-24"

                else:

                    return "The input letter grade is outside the range supported"
        
        else:

            return "Input value must be a number or a letter"



        

    


        


'''

#Exercise 4

For fizz_buzz(), I want you to add error handling (exception handling)

to catch those casting issues, or non-type issue, 

and use this to return the error message, 'Input value(s) must be a number', for the function.

'''
'''
function takes in 3 parameters and returns fizz, buzz or fizzbuzz based on the above criteria

returns an error if any values are not a number

'''
                


def fizz_buzz(num1, divisor_1=3,divisor_2=5):
    
    try:
                
        
            
            if( num1%divisor_1 == 0 and num1%divisor_2 == 0 ): #both are multiples of 3 and 5

                        return "FizzBuzz"

            elif( num1%divisor_1 != 0 and num1%divisor_2 != 0 ): #none are multiples of 3 and 5

                        return num1


            elif(num1%divisor_1 == 0): #is num1 a multiple of 3

                        return "Fizz"

            elif(num1%divisor_2 == 0): #is num1 a multiple of 5

                        return "Buzz"

    except Exception as e:

        return ("Input value(s) must be a number")
        
        #return ("Input value(s) must be a number or a divisor is zero: ",e) #more specific error message


    

        
            








    

            

    
 
    









    

    


 



   





