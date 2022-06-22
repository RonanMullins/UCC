from flask import Flask, render_template, request, session, redirect, url_for, g, request, jsonify
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

@app.route("/login", methods=["GET","POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user_id = form.user_id.data
        password = form.password.data
        db = get_db()
        matching_user = db.execute("""SELECT * FROM users WHERE user_id = ?""", (user_id,)).fetchone()
        if matching_user is None:
            form.user_id.errors.append("Unknown user.")
        elif not check_password_hash(matching_user["password"], password):
            form.password.errors.append("Password is incorrect.")
        else:
            session.clear()
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
        db = get_db()
        possible_clashing_user = db.execute("""SELECT * FROM users WHERE user_id = ?""", (user_id,)).fetchone()
        if possible_clashing_user is not None:
            form.user_id.errors.append("This user id is taken.")
        else:
            db.execute("""INSERT INTO users (user_id, password) VALUES (?, ?);""",(user_id, generate_password_hash(password)))
            db.commit()
            return redirect(url_for("login"))         
    return render_template("register.html", form=form)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/survival")
@login_required
def survival():
    return render_template("survival.html")

@app.route("/leaderboard", methods=["GET","POST"])
def leaderboard():
    db = get_db()
    players = db.execute("""SELECT * FROM leaderboard ORDER BY score DESC;""").fetchall()
    db.commit() 
    return render_template("leaderboard.html", players=players)

@app.route("/store_score", methods=["POST"])
@login_required
def store_score():
    user_id = session['user_id']
    score = int(request.form["score"])
    time = float(request.form["time"])
    db = get_db()
    db.execute("""INSERT INTO leaderboard (user_id, score, time) VALUES (?, ?, ?);""",(user_id, score, time))
    db.commit()
    return "success"
