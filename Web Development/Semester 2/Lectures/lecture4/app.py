from urllib import response
from flask import Flask, render_template, request 

app = Flask(__name__)

@app.route("/greet_me", methods=["GET","POST"])
def send_greeting():
    if request.method == "GET":
        return render_template("form.html")
    else: #i.e a POST request
        given_name = request.form["given_name"]
        family_name = request.form["family_name"]
        return render_template("response.html", given_name=given_name, family_name=family_name)