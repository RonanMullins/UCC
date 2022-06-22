from flask import Flask, render_template
from database import get_db, close_db
from forms import EuroForm, AKEForm

app = Flask(__name__)
app.config["SECRET_KEY"] = "this-is-my-secret-key"
app.teardown_appcontext(close_db)

@app.route("/winners", methods=["GET","POST"])
def winners():
    form = EuroForm()
    winners = None
    if form.validate_on_submit():
        country = form.country.data
        db = get_db()
        winners = db.execute("""SELECT * FROM winners WHERE country = ?;""", (country,)).fetchall()
        country_exist = db.execute("""SELECT * FROM winners WHERE country = ?;""", (country,)).fetchone()
        if country_exist == None:
            form.country.errors.append("This Country Does Not Exist in The Database")

    return render_template("winners.html", form=form, caption="Eurovision Winners", winners=winners)

@app.route("/min_winners", methods=["GET","POST"])
def min_winners():
    form = AKEForm()
    winners = None
    
    if form.validate_on_submit():

        db = get_db()
        country = form.country.data
        points = form.points.data

        if country != "" and points == "":

            winners = db.execute("""SELECT * FROM winners WHERE country = ?;""", (country,)).fetchall()

        if points != "" and country == "":

            winners = db.execute("""SELECT * FROM winners WHERE points >= ?;""", (points,)).fetchall()

        if points != "" and country != "":

            winners = db.execute("""SELECT * FROM winners WHERE country = ? AND points >= ?;""", (country,points,)).fetchall()

        if points == "" and country == "":

            winners = db.execute("""SELECT * FROM winners;""").fetchall()
    

    return render_template("min_winners.html", form=form, caption="Eurovision Winners", winners=winners)
