from genericpath import exists
from urllib import response
from flask import Flask, render_template, request 
from forms import DSMForm

app = Flask(__name__)
app.config["SECRET_KEY"] = "this-is-my-secret-key"

@app.route("/spy", methods=["GET","POST"])

def bond_intro():
    if request.method == "GET":
        return render_template("form.html")

    else:
        given_name = request.form["given_name"]
        family_name = request.form["family_name"]
        return render_template("response.html", given_name=given_name, family_name=family_name)

@app.route("/morse", methods=["GET", "POST"])

def morse():

    if request.method == "GET":

        return render_template("morse_form.html")

    else:

        message = request.form["message"]
        cleaned_message = message.strip().upper()
        morse= ""
        morse_dict = {

                    "A":".-", "B":"-...",
                    "C":"-.-.", "D":"-..", "E":".",
                    "F":"..-.", "G":"--.", "H":"....",
                    "I":"..", "J":".---", "K":"-.-",
                    "L":".-..", "M":"--", "N":"-.",
                    "O":"---", "P":".--.", "Q":"--.-",
                    "R":".-.", "S":"...", "T":"-",
                    "U":"..-", "V":"...-", "W":".--",
                    "X":"-..-", "Y":"-.--", "Z":"--..",
                    "1":".----", "2":"..---", "3":"...--",
                    "4":"....-", "5":".....", "6":"-....",
                    "7":"--...", "8":"---..", "9":"----.",
                    "0":"-----"," ": "/"

        }
        if message is "":

            return render_template("morse_response.html", message="", morse="", error="No message entered!")

        if message not in morse_dict:

            return render_template("morse_response.html", message="", morse="", error="Character not in dictionary!")


        for char in cleaned_message:

            code = morse_dict[char]
            morse = morse + code

        return render_template("morse_response.html", message=message, morse=morse)

@app.route("/lengths", methods=["GET", "POST"])


def dsm():

    if request.method == "GET":
        return render_template("dsm_form.html",inches="", centimetres="")

    else:

        inches = request.form.get("inches")
        centimetres = request.form.get("centimetres")
        

        if inches == "" and centimetres == "":
            return render_template("dsm_form.html", error="Must input a value")
        
        elif not inches == "" and not centimetres == "":

            return render_template("dsm_form.html", error="Must input one value")

        else:
    
            if inches == "":
                centimetres = float(centimetres)
                inches = centimetres * 2.54
                return render_template("dsm_response.html", inches=inches, centimetres="")

            
            elif centimetres == "":
                inches = float(inches)
                centimetres = inches / 2.54
                return render_template("dsm_response.html", inches="", centimetres=centimetres)


            return render_template("dsm_response.html")


