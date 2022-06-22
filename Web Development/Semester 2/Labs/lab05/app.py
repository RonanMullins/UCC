import imp
from flask import Flask, render_template, redirect, url_for, session
from flask_session import Session
from forms import GuessForm

app = Flask(__name__)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@app.route("/guess")
def guess_number():

    if request.cookies.get("voted") == "yes":

        return render_template("response.html", message = "Sorry! You already voted")

    form = GuessForm()
    if form.validate_on_submit():

        return render_template(".html", form=form, message="")




