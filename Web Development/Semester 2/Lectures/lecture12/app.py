from dataclasses import dataclass
from flask import Flask, render_template, request, session, redirect, url_for, g, request
from database import get_db, close_db
from flask_session import Session
from werkzeug.security import generate_password_hash, check_password_hash
from forms import RegistrationForm, LoginForm
from functools import wraps

app = Flask(__name__)
app.teardown_appcontext(close_db)
app.config["SECRET_KEY"] = "this-is-my-secret-key"
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@app.before_request
def load_logged_in_user():
    g.user = session.get("user_id", None)

def login_required(view):
    @wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for("login", next=request.url))
        return view(**kwargs)
    return wrapped_view

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login", methods=["GET","POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user_id = form.user_id.data
        password = form.password.data
        db = get_db()
        matching_user = db.execute("""SELECT * FROM users WHERE user_id = ?""", (user_id,)).fetchone()
        if matching_user is None:
            form.user_id.errors.append("Unknown user id!")
        elif not check_password_hash(matching_user["password"], password):
            form.password.errors.append("Incorrect password!")
        else:
            session.clear() #cookies clear
            session["user_id"] = user_id
            next_page = request.args.get("next")
            if not next_page:
                next_page = url_for("index")
            return redirect( next_page )
    return render_template("login.html", form=form)

@app.route("/logout")
def logout():
    session.clear()
    return redirect( url_for("index") )

@app.route("/register", methods=["GET","POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user_id = form.user_id.data
        password = form.password.data
        password2 = form.password2.data
        db = get_db()
        possible_clashing_user = db.execute("""SELECT * FROM users WHERE user_id = ?""", (user_id,)).fetchone()
        if possible_clashing_user is not None:
            form.user_id.errors.append("User id already taken!")
        else:
            db.execute("""INSERT INTO users (user_id, password) VALUES (?, ?);""",(user_id, generate_password_hash(password)))
            db.commit()
            return redirect(url_for("login"))         
    return render_template("register.html", form=form)

@app.route("/wines")
def wines():
    db = get_db()
    wines = db.execute("""SELECT * FROM wines;""").fetchall()
    return render_template("wines.html", wines=wines)

@app.route("/wine/<int:wine_id>")
def wine(wine_id):
    db = get_db()
    wine = db.execute("""SELECT * FROM wines WHERE wine_id = ?;""", (wine_id,)).fetchone()
    return render_template("wine.html", wine=wine)

@app.route("/cart")
@login_required
def cart():
    #show the cart
    if "cart" not in session:
        session["cart"] = {}
    names = {}
    db = get_db()
    for wine_id in session["cart"]:
        wine = db.execute("""SELECT * FROM wines WHERE wine_id =  ?;""", (wine_id,)).fetchone()
        name = wine["name"]
        names[wine_id] = name
    return render_template("cart.html", cart=session["cart"], names=names)

@app.route("/add_to_cart/<int:wine_id>")
@login_required
def add_to_cart(wine_id):
    #add one bottle of wine_id to the cart 
    if "cart" not in session:
        session["cart"] = {}
    if wine_id not in session["cart"]:
        session["cart"][wine_id] = 0

    session["cart"][wine_id] = session["cart"][wine_id] + 1


    return redirect( url_for("cart"))