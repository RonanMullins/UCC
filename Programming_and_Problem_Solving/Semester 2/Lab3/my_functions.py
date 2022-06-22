# ScriptName: my_functions.py
# Author: Ronan Mullins 121107333

from multiprocessing import cpu_count
from random import randint

def ships(numShip:int = 2)->list:
    '''
    takes in the number of ships, returns a list called my_ships
    '''
    # let's start by randomly selecting 'numShip' space ships
    # numShip should have a default value of 2

    # let's choose from the following 5 ships:
    # Enterprise, Galactica, Rocinante, Serenity and RazorCrest

    try:

        spaceships = ["Enterprise", "Galactica", "Rocinante", "Serenity","RazorCrest"] #define spaceships

        my_ships = []

        for x in range(numShip):

            my_ships.append(spaceships[randint(0,4)]) #add a random spaceship for every number of ship 

        return my_ships

    except:

        return "Oops"

def crews(ships:list, crew:list = ["captain","first_mate","mechanic"])->list:
    '''
    takes in a list of ships and what crew to be returned
    '''
    # for each of the 'ships' we need a crew
    # by default, the crew should be composed of a captain, a first_mate and the name of the person who fixes the engines

    # the 'crew' param is a list of the crew to return
    # it must contain one crew title, and a maximum of three crew titles

    try:

        #define all captains,first mates and mechanics
        captain = ["Shlug","Francis","Fr.Ted","Batman","Hawkeye"]
        first_mate = ["Nick Frost","Simon Pegg","Thor","Andy from accounts","Snoop Dogg"]
        mechanic = ["Claptrap","Captain Birdseye","Wesley","Tom Hanks","Gordon Ramsey"]

        selected_crew = []

        if "captain" in crew:

            for x in ships:

                selected_crew.append(captain[randint(0,4)]) #if captain, add a random captain for every ship

        if "first_mate" in crew:

            for x in ships:

                selected_crew.append(first_mate[randint(0,4)]) #if first mate, add a random first mate for every ship

        if "mechanic" in crew:

            for x in ships:

                selected_crew.append(mechanic[randint(0,4)]) #if mechanic, add a random mechanic for every ship

        return selected_crew #return the crew

    except:

        return "Oops"

def destinations(ships:list)->list:
    '''
    takes in a list of ships and returns a destination for each ship
    '''
    # for each of the 'ships' we need a destination
    # find 3 destinations the ship has been to and randomly return 1 of them

    try:

            
        my_destinations = ["Dublin", "Cork", "Paris","Mars","Saturn"] #define the destinations
        selected_destinations = []

        for x in ships:

            selected_destinations.append(my_destinations[randint(0,3)]) #for every ship, add a random destination to selected destinations list

        return selected_destinations

    except:

        return "Oops"

def recur_func(count:int,count_list:list=[])-> list:
    '''
    Recursive function which counts down from 5 to 0, returns in the form of a list
    '''

    try:

        if count == 0:
            return count_list #if the count is zero then return the list
        else:
            count_list.append(count) #add the count to the list
            recur_func(count-1,count_list)    #recursive call, reduce the count by one and pass through the updated list
        return count_list
        
    except:

        return "Oops"

def countDown(ships:list, my_destinations:list)->str:
    '''
    takes in a list of ships and a list of destintations, returns a formatted string of what ship blasted off and its destination

    '''
    # each of the ships needs to blast off, so let's count them down
    # for each ship, create a string using the following format
    # 5, 4, 3, 2, 1 - <ship> has blasted off to <destination> using a <loop_type> loop

    # the first ship should use a for loop
    # the second ship should use a while loop
    # the third ship should use recursion - using the recur_func()
    # and repeat, fourth ship uses a for loop, etc...
    try:

        #define the output string and all its lines. define the countdown string (5,4,3,2,1)
        output_str = ""
        l1= ""
        l2= ""
        l3= ""
        l4= ""
        l5= ""
        c_down = ""
        
        if len(ships) >= 1: #1st ship

            c_down = ""

            for x in range(5,0,-1): #go through this backwards
                
                c_down = c_down + str(x) + ", " #add x to the c_down string

            l1 = c_down + str(ships[0]) + " has blasted off to " + str(my_destinations[randint(0,4)]) + " using a for loop " #format the line output

        if len(ships) >= 2: #2nd ship

            x = 4
                
            while x < 4: #define x while its less than 4

                c_down = c_down + str(x) + ", "  #add x to the c_down string
                x+=1

            l2 = c_down + str(ships[1]) + " has blasted off to " + str(my_destinations[randint(0,4)]) + " using a while loop " #format the line output

        if len(ships) >= 3: #3rd ship

            c_down_str = ""
            c_down = recur_func(5) #call the recursive function

            for x in range(0,5):

                c_down_str = c_down_str + str(c_down[x]) + ", " #unpack the list elements as strings, add x to the c_down string

            l3 = c_down_str + str(ships[2]) + " has blasted off to " + str(my_destinations[randint(0,4)]) + " using a recursive loop " #format the line output

        if len(ships) >= 4: #4th ship

            c_down = ""

            for x in range(5,0,-1):
                
                c_down = c_down + str(x) + ", " #add x to the c_down string

            l4 = c_down + str(ships[3]) + " has blasted off to " + str(my_destinations[randint(0,4)]) + " using a for loop " #format the line output

        if len(ships) >= 5: #5th ship 

            x = 4
                
            while x < 4: #define x while its less than 4

                c_down = c_down + str(x) + ", " #add x to the c_down string
                x+=1

            l5 = c_down + str(ships[4]) + " has blasted off to " + str(my_destinations[randint(0,4)]) + " using a while loop " #format the line output
        
        output_str = l1 +"\n"+ l2 +"\n"+ l3 +"\n"+ l4 +"\n"+ l5 #format the line output
        return output_str

    except:

        return "Oops"

def printout(ships:list, crews:list, destinations:list, format:str="capatalise")->str:
    '''
    take in multiple lists and return a formatted string 
    '''
    # for each ship, create a string composed of the name of the ship,
    # their crew and their destination, in the format:
    # <ship> has a crew of <crew> and is on route to <destination>
    # one ship string per line

    # 'format' should have a default value of "capatalise",
    # but can also take other formats, "lower", "upper", etc

    try:

        #define the lines for formatted output
        l1= ""
        l2= ""
        l3= ""
        l4= ""
        l5= ""
        output = ""

        if len(ships) >= 1: #1 ship

            if format == "capatalise":

                l1 = ships[0]+" has a crew of "+crews[0]+" and is on route to "+destinations[0] #format the line
                l1 = l1.capitalize() #capitalize the string

            if format == "lower":

                l1 = ships[0]+" has a crew of "+crews[0]+" and is on route to "+destinations[0] 
                l1 = l1.lower() #lower case the string

            if format == "upper":

                l1 = ships[0]+" has a crew of "+crews[0]+" and is on route to "+destinations[0]
                l1 = l1.upper() #uppercase the string

        if len(ships) >= 2: #2 ships

            if format == "capatalise":

                l2 = ships[1]+" has a crew of "+crews[1]+" and is on route to "+destinations[1] #format the line
                l2 = l2.capitalize()

            if format == "lower":

                l2 = ships[1]+" has a crew of "+crews[1]+" and is on route to "+destinations[1]
                l2 = l2.lower()

            if format == "upper":

                l2 = ships[1]+" has a crew of "+crews[1]+" and is on route to "+destinations[1]
                l2 = l2.upper()


        if len(ships) >= 3: #3 ships

            if format == "capatalise":

                l3 = ships[2]+" has a crew of "+crews[2]+" and is on route to "+destinations[2] #format the line
                l3 = l3.capitalize()

            if format == "lower":

                l3 = ships[2]+" has a crew of "+crews[2]+" and is on route to "+destinations[2]
                l3 = l3.lower()

            if format == "upper":

                l3 = ships[2]+" has a crew of "+crews[2]+" and is on route to "+destinations[2]
                l3 = l3.upper()


        if len(ships) >= 4: #4 ships

            if format == "capatalise":
 
                l4 = ships[3]+" has a crew of "+crews[3]+" and is on route to "+destinations[3] #format the line
                l4 = l4.capitalize()

            if format == "lower":

                l4 = ships[3]+" has a crew of "+crews[3]+" and is on route to "+destinations[3]
                l4 = l4.lower()

            if format == "upper":

                l4 = ships[3]+" has a crew of "+crews[3]+" and is on route to "+destinations[3]
                l4 = l4.upper()


        if len(ships) >= 5: #5 ships

            if format == "capatalise":

                l5 = ships[4]+" has a crew of "+crews[4]+" and is on route to "+destinations[4] #format the line
                l5 = l5.capitalize()

            if format == "lower":

                l5 = ships[4]+" has a crew of "+crews[4]+" and is on route to "+destinations[4]
                l5 = l5.lower()

            if format == "upper":

                l5 = ships[4]+" has a crew of "+crews[4]+" and is on route to "+destinations[4]
                l5 = l5.upper()



        output = l1 +"\n"+ l2 +"\n"+ l3 +"\n"+ l4 +"\n"+ l5 #format each line with new lines
        return output

    except:

        return "Oops"

def toInfinityAndBeyond():
    '''
    Function used to call every other function in the file
    '''

    try:

        # an example of how I could call the helper functions is shown below

        # variables for ships, crews and destinations
        my_ships = []
        my_crews = []
        my_destinations = []
        my_numShips = 3

        # save 3 ships
        my_ships = ships(my_numShips)

        # # save 1 crew members for each ship
        my_crews = crews(my_ships, ["captain"])

        # # save 1 destination for each ship
        my_destinations = destinations(my_ships)

        # each of the ships needs to blast off, so lets count them down
        print(countDown(ships, my_destinations))

        # produce a string we can return
        return printout(my_ships, my_crews, my_destinations, "lower")

    except:

        return "Oops"


