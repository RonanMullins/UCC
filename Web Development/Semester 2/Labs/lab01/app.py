# from flask import Flask, render_template
# import random

# app = Flask(__name__)

# @app.route("/rps/<player>")

# def rps(player):

#     c_ans = random.randint(1,3)

#     if(c_ans == 1):
#         c_ans = "rock"

#     if(c_ans == 2):
#         c_ans = "paper"

#     if(c_ans == 3):
#         c_ans = "scissors"

#     if(c_ans == player):

#         return render_template("It's a draw")

#     if(c_ans == "rock")and(player == "scissors"):

#         return render_template("Computer wins!")

#     if(c_ans == "paper")and(player == "rock"):

#         return render_template("Computer wins!")

#     if(c_ans == "scissors")and(player == "paper"):

#         return render_template("Computer wins!")
    
#     if(c_ans == "scissors")and(player == "rock"):

#         return render_template("Player wins!")

#     if(c_ans == "rock")and(player == "paper"):

#         return render_template("Player wins!")

#     if(c_ans == "paper")and(player == "scissors"):

#         return render_template("Player wins!")

# def rps(player):

#     c_ans = random.randint(1,3)

#     # player = render_template("rps.html", p_weapon = player)
    
#     if(player == "rock"):
        
#        return render_template("rps.html", p_weapon = player)
    
#     if(player == "paper"):
        
#         return render_template("rps.html", p_weapon = player)

#     if(player == "scissors"):
        
#         return render_template("rps.html", p_weapon = player)

#     if(c_ans == 1):
#         c_ans = "rock"
#         return render_template("rps.html", c_weapon = c_ans)

#     if(c_ans == 2):
#         c_ans = "paper"
#         return render_template("rps.html", c_weapon = c_ans)

#     if(c_ans == 3):
#         c_ans = "scissors"
#         return render_template("rps.html", c_weapon = c_ans)


#     if(c_ans == player):

#         res = "It's a draw"
#         return render_template("rps.html", winner = res )

#     if(c_ans == "rock")and(player == "scissors"):

#         res = "Computer wins!"
#         return render_template("rps.html", winner = res )

#     if(c_ans == "paper")and(player == "rock"):

#         res = "Computer wins!"
#         return render_template("rps.html", winner = res )

#     if(c_ans == "scissors")and(player == "paper"):

#         res = "Computer wins!"
#         return render_template("rps.html", winner = res )
    
#     if(c_ans == "scissors")and(player == "rock"):

#         res = "Player wins!"
#         return render_template("rps.html", winner = res )

#     if(c_ans == "rock")and(player == "paper"):

#         res = "Player wins!"
#         return render_template("rps.html", winner = res )

#     if(c_ans == "paper")and(player == "scissors"):

#         res = "Player wins!"
#         return render_template("rps.html", winner = res )


from unittest import result
from flask import Flask, render_template
import random

from random import randint

app = Flask(__name__)

@app.route("/rps/<player>")

#problem 1&2

def rps(player):

    c_ans = random.randint(1,3)

    if(c_ans == 1):
        c_ans = "rock"

    if(c_ans == 2):
        c_ans = "paper"

    if(c_ans == 3):
        c_ans = "scissors"

    if(c_ans == player):

        res = "It's a draw"

    if(c_ans == "rock")and(player == "scissors"):

        res = "Computer wins!"

    if(c_ans == "paper")and(player == "rock"):

        res = "Computer wins!"

    if(c_ans == "scissors")and(player == "paper"):

        res = "Computer wins!"
    
    if(c_ans == "scissors")and(player == "rock"):

        res = "Player wins!"

    if(c_ans == "rock")and(player == "paper"):

        res = "Player wins!"


    if(c_ans == "paper")and(player == "scissors"):

        res = "Player wins!"


    return render_template("rps.html", winner = res, c_weapon = c_ans, p_weapon = player)

#problem 3&4

@app.route("/could_it_be_me")
@app.route("/could_it_be_me/<int:num_lines>")

def send_lotto_numbers(num_lines):

    line = []
    lotto_numbers = []

    if num_lines == 1:

        for i in range(0, 6):

            n = randint(1, 47)
            line.append(n)

    else:
        
        while len(lotto_numbers) < num_lines:
        
            while len(line) < 6:

                n = randint(1, 47)
                if n not in line:
                    line.append(n)

            lotto_numbers.append(line)
        
    return render_template("lotto.html", lotto_numbers=lotto_numbers, line=line)+"\n"


    # return render_template("lotto.html", line=line)
 



