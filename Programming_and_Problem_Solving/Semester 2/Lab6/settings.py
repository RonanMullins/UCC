# ScriptName: settings.py
# Author: Ronan Mullins 121107333

# settings for your tests

# ===================================================
# functions to call
test_func = ["difference_of_numbers" # difference_of_numbers
            ]

# ===================================================
# input parameter(s) and values to pass to the functions
param_name = [
              # difference_of_numbers
              ["characters"]
             ]

input_vals = [
              # difference_of_numbers with one param
              [ ["1"],["123"],["a"],["2a2"],["3A2"],["1gibberish5"],["8aa10aa"],["1!£$%^2&*()_+3"],[True],[[]]
              ]
             ]

# ===================================================
# output values I must test against for this function
outputlist = [
              # difference_of_numbers
              [ "Difference of numbers = 1","Difference of numbers = 123","No numbers in the sequence!","Difference of numbers = 2","Difference of numbers = 7",
                "Difference of numbers = -3","Difference of numbers = 9","Difference of numbers = 6","difference_of_numbers() Problem! Input must not be a boolean value!",
                "difference_of_numbers() Problem! Input must be a str!"
              ]
             ]
