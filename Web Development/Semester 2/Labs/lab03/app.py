from flask import Flask, render_template
from forms import CipherForm, ConversionForm

app = Flask(__name__)
app.config["SECRET_KEY"] = "this-is-my-secret-key"

@app.route("/shift", methods=["GET", "POST"])

def cipher():

    form = CipherForm()

    if form.validate_on_submit(): #if the request is a post request and if data validates

        plaintext = form.plaintext.data
        shift = form.shift.data
        ciphertext = ""


        for char in plaintext:
            if char.isupper():
                ciphertext += chr((ord(char) - 65 + shift) % 26 + 65)
            elif char.islower():
                ciphertext += chr((ord(char) - 97 + shift) % 26 + 97)
            else:
                ciphertext += char

        form.ciphertext.data = ciphertext
        
    return render_template("shift_form.html", form=form)


@app.route("/conversion", methods=["GET", "POST"])

def conversion():

    form = ConversionForm()

    if form.validate_on_submit(): #if the request is a post request and if data validates

        fahrenheit_from = form.fahrenheit_from.data
        celsius_from = form.celsius_from.data
        kelvin_from = form.kelvin_from.data
        input = form.input.data

        fahrenheit_to = form.fahrenheit_to.data
        celsius_to = form.celsius_to.data
        kelvin_to = form.kelvin_to.data
        answer = 0.0

        if celsius_from == True and fahrenheit_to == True:

            answer = 9 / 5 * input + 32
            form.answer.data = answer

        if kelvin_from == True and fahrenheit_to == True:

            answer = 9 / 5 * (input-273) + 32
            form.answer.data = answer
        
        if fahrenheit_from == True and celsius_to == True:

            answer = 5 / 9 * (input-32)
            form.answer.data = answer

        if celsius_from == True and kelvin_to == True:

            answer = input + 273
            form.answer.data = answer

        if kelvin_from == True and celsius_to == True:

            answer = input - 273
            form.answer.data = answer

        if fahrenheit_from == True and kelvin_to == True:

            answer = 5 / 9 * (input - 32) + 273
            form.answer.data = answer
        
    return render_template("conversion_form.html", form=form)
