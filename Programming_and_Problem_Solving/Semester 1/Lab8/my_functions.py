# ScriptName: my_functions.py
# Author: Ronan Mullins 121107333

import random

'''
Question 2 
'''

def while_loop(max_number = None):

    try:

        my_list = []

        if(max_number is None):
        
            i=1
            acc=0
            while i<=10:

                if(i>12):

                    break

                my_list.append(i)
                acc+=i
                i+=1
            
            

            my_list.append(acc)
            return my_list

        elif(max_number < 0):

            i=1
            acc=0
            while max_number<= i:

                if(i<-12):
                
                    break

                my_list.append(i)
                acc+=i
                i-=1

            my_list.append(acc)
            return my_list

        elif(max_number >= 0):

            i=1
            acc=0
            while i<=max_number:

                if(i>12):
                  
                    break

                my_list.append(i)
                acc+=i
                i+=1

            my_list.append(acc)
            return my_list

    except:

        return "“Did you break the break or should we continue?"



'''
Question 3
'''

def magic_8_ball(my_question = "", fixed_list = None): 

    ans_list = ["It is certain.","It is decidedly so.","Without a doubt.","Yes definitely.","You may rely on it.","As I see it, yes.","Most likely.","Outlook good.","Yes.","Signs point to yes.",
                "Reply hazy, try again.","Ask again later.","Better not tell you now.","Cannot predict now.","Concentrate and ask again.",
                "Don't count on it.","My reply is no.","My sources say no.","Outlook not so good.","Very doubtful."]
    try:
        
        if type(fixed_list)==list and -1 in fixed_list:

            return 2/"eggs"

    except Exception as e:

        return "Error ocurred: ",e

    try:

        if(fixed_list is None):
    
            return ans_list[random.randint(0,19)]

        else:

            new_list = []
            i = 0

            while i < len(fixed_list):
            
                new_list.append(fixed_list[i])
                i += 1

            if(len(new_list)<=1): #check this

                return ans_list[new_list[0]]

            elif(len(new_list)>1):

                return ans_list[new_list[random.randint(0,len(new_list)-1)]]

    except:

        return "I have spoken."



'''
Question 4
'''

def all_pairs(s1 =[], s2 =[]):

    try:

        pair_list=[]

        for i in s1:

            for j in s2:

                pair_list.append(str(i)+str(j))
            
        return False, pair_list


    except Exception:

        return True, [-1]








     
