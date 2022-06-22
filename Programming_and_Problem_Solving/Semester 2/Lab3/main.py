# ScriptName: main.py
# Author: Ronan Mullins 121107333

from my_functions import *


def main():
    """
    Call the functions defined in the functions.py file
    """
    # #ships
    # print(ships(3)) #working needs to be tested

    # # #crews
    # print(crews(["Enterprise", "Galactica"],["captain"])) #working needs to be tested

    # # # #destinations
    # print(destinations(["Enterprise", "Galactica"])) #working needs to be tested

    # #recur
    # print(recur_func(5))

    # #countdown
    print(countDown( ["Enterprise", "Galactica"],["Dublin", "Cork", "Paris","Mars","Saturn"])) #not working

    # #printout
    # print(printout(["Enterprise", "Galactica", "Rocinante", "Serenity","RazorCrest"],["Shlug","Francis","Fr.Ted","Batman","Hawkeye"],["Dublin", "Cork", "Paris","Mars","Saturn"]))

    # print(toInfinityAndBeyond())



if __name__ == "__main__":
    ''' call the main() function in this file '''
    main()
