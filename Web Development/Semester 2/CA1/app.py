from dataclasses import dataclass
from email import message
from flask import Flask, render_template, request, session, redirect, url_for, g, request
from database import get_db, close_db
from flask_session import Session
from werkzeug.security import generate_password_hash, check_password_hash
from forms import RegistrationForm, LoginForm, ContactForm, AddForm, RemoveForm, OrderForm, RemoveOrderForm
from functools import wraps
from datetime import datetime, timedelta 

app = Flask(__name__)
app.teardown_appcontext(close_db)
app.config["SECRET_KEY"] = "this-is-my-secret-key"
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

'''
Admin login details
User_id = admin
password = 123

If there is any issues with the admin account. register as admin with the password 123

The admin can:
view all messages received from the "Contact us" page.
add/remove products from the shop.
cancel orders.
tables in the admin section contain an amend column used to remove products and orders.

A regular user can:
browse instruments.
add instruments to their cart.
clear their cart.
apply discount at checkout
make an order.
visit their profile to view an order.
delete their account.
contact the admin via "Contact us".

use the 20% off discount code: SHRED when you spend 50 euro.

had some issues with elements going off screen. the "admin" and "contact us" links especially. zooming in on the browser should show the elements. 

'''

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

@app.route("/instruments")
def instruments():
    db = get_db()
    instruments = db.execute("""SELECT * FROM instruments;""").fetchall()
    heading = "All Instruments"
    return render_template("instruments.html", instruments=instruments, heading=heading)

@app.route("/instrument/<int:instrument_id>")
def instrument(instrument_id):
    db = get_db()
    instrument = db.execute("""SELECT * FROM instruments WHERE instrument_id = ?;""", (instrument_id,)).fetchone()
    return render_template("instrument.html", instrument=instrument)

@app.route("/electric_guitars")
def electric_guitars():
    db = get_db()
    instruments = db.execute("""SELECT * FROM instruments WHERE category = 'electric guitar';""").fetchall()
    heading = "All Electric Guitars"
    return render_template("instruments.html", instruments=instruments, heading=heading)

@app.route("/acoustic_guitars")
def acoustic_guitars():
    db = get_db()
    instruments = db.execute("""SELECT * FROM instruments WHERE category = 'acoustic guitar';""").fetchall()
    heading = "All Acoustic Guitars"
    return render_template("instruments.html", instruments=instruments, heading=heading)

@app.route("/wind_instruments")
def wind_instruments():
    db = get_db()
    instruments = db.execute("""SELECT * FROM instruments WHERE category = 'wind';""").fetchall()
    heading = "All Wind Instruments"
    return render_template("instruments.html", instruments=instruments, heading=heading)

@app.route("/cart")
@login_required
def cart():
    if "cart" not in session:
        session["cart"] = {}
    if "quantity" not in session:
        session["quantity"] = {}

    images = {}
    names = {}
    prices = {}
    total = 0
    db = get_db()
    for instrument_id in session["cart"]:
        instrument = db.execute("""SELECT * FROM instruments WHERE instrument_id =  ?;""", (instrument_id,)).fetchone()
        image = instrument["image"]
        images[instrument_id] = image
        name = instrument["name"]
        names[instrument_id] = name
        price = instrument["price"]
        prices[instrument_id] = price
        total = total + float(prices[instrument_id])
    total = round(total,2)
    return render_template("cart.html", cart=session["cart"], name=names, price=prices, total=total, image=images)

@app.route("/add_to_cart/<int:instrument_id>")
@login_required
def add_to_cart(instrument_id):
    if "cart" not in session:
        session["cart"] = {}
        session["quantity"] = {}

    if instrument_id not in session["cart"]:
        session["cart"][instrument_id] = 0

    if instrument_id not in session["quantity"]:
        session["quantity"][instrument_id] = 0

    session["cart"][instrument_id] = session["cart"][instrument_id] + 1
    session["quantity"][instrument_id] = session["quantity"][instrument_id] + 1

    return redirect( url_for("cart"))

@app.route("/clear_cart")
@login_required
def clear_cart():
    session.pop('cart')
    return redirect( url_for("cart"))

@app.route("/contact", methods=["GET","POST"])
@login_required
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        message = form.message.data
        db = get_db()
        db.execute("""INSERT INTO contact (name, email, message) VALUES (?, ?, ?);""",(name, email, message))
        db.commit() 
        return redirect(url_for("contact"))  
    return render_template("contact.html", form=form)

@app.route("/admin", methods=["GET","POST"])
@login_required
def admin():

    if session['user_id'] == 'admin':
        db = get_db()
        messages = db.execute("""SELECT * FROM contact;""").fetchall()
        db.commit() 
        return render_template("admin_page.html", messages=messages)
    else:
        return redirect(url_for("index"))

@app.route("/clear_contact", methods=["GET","POST"])
@login_required
def clear_contact():
    db = get_db()
    db.execute("""DELETE FROM contact;""").fetchall()
    db.commit() 
    return render_template("admin_page.html")

@app.route("/add_instrument", methods=["GET","POST"])
@login_required
def add_instrument():
    db = get_db()
    instruments = db.execute("""SELECT * FROM instruments;""").fetchall()
    db.commit()
    form = AddForm()
    if form.validate_on_submit():
        add_name = form.add_name.data
        add_type = form.add_type.data
        add_price = form.add_price.data
        add_description = form.add_description.data
        image_file = form.image_file.data
        db.execute("""INSERT INTO instruments (name, category, price, description, image) VALUES (?, ?, ?, ?,?);""",(add_name, add_type, add_price, add_description, image_file))
        db.commit()
        return redirect(url_for("add_instrument"))
    return render_template("add_instrument.html", form=form, instruments=instruments)

@app.route("/remove_instrument", methods=["GET","POST"])
@login_required
def remove_instrument():
    db = get_db()
    instruments = db.execute("""SELECT * FROM instruments;""").fetchall()
    db.commit()
    return render_template("remove_instrument.html", instruments=instruments)

@app.route("/checkout", methods=["GET","POST"])
@login_required
def checkout():
    '''
    if the form validates. take the information from the session and the form to insert into the orders table.
    check for the method of delivery and apply the appropriate charges. Also calculate the date at which the order will be delivered.
    make a 20% discount if the user uses the code SHRED.
    '''
    if "cart" not in session:
        session["cart"] = {}
        session["quantity"] = {}
    form = OrderForm()
    if form.validate_on_submit():
        names = ""
        categories = ""
        str_of_prices = ""
        total = 0.0
        discount = 0.0 
        before_shipping = 0.0
        before_discount = 0.0
        message = ""
        delivery_date = ""
        prices = {}
        user_id = session['user_id']
        discount_code = form.discount_code.data
        first_name = form.first_name.data 
        last_name = form.last_name.data 
        address = form.address.data 
        delivery_type = form.delivery.data
    
        for instrument_id in session["cart"]:
            db = get_db()
            instrument = db.execute("""SELECT * FROM instruments WHERE instrument_id =  ?;""", (instrument_id,)).fetchone()
            db.commit()

            for x in session["quantity"]:
            

                names = str(names) + " " + str(instrument['name'])
                categories = categories + " " + instrument['category']
                str_of_prices = str(str_of_prices) + " " + str(instrument['price'])
                price = instrument["price"] #total tally
                prices[instrument_id] = price
                amount = price * x
                total = total + amount

            before_shipping = total #shipping
            if form.delivery.data == "Standard Delivery (€3)":
                total = total + 3
                shipping = 3
                delivery_date = datetime.now() + timedelta(days=5)
                delivery_date  = delivery_date.strftime("%d-%m-%y")
                message = "Your delivery will be with you by "+ delivery_date
            if form.delivery.data == "Next-Day Delivery (€12)":
                total = total + 12
                shipping = 12
                delivery_date = datetime.now() + timedelta(days=1)
                delivery_date  = delivery_date.strftime("%d-%m-%y")
                message = "Your delivery will be with you on "+ delivery_date

            before_discount = total #discount
            if total >= 50:
                    if discount_code == "SHRED":
                        discount = (20 * total) / 100
                        total = total - discount

            before_shipping = round(before_shipping,2)
            before_discount = round(before_discount,2)
            total = round(total,2)
            discount = round(discount,2)
            db = get_db()
            db.execute("""INSERT INTO orders (user_id, first_name, last_name, address, delivery_type, delivery_date, instrument_id, names, categories, prices, total) VALUES (?,?,?,?,?,?,?,?,?,?,?);""",(user_id, first_name, last_name, address, delivery_type, delivery_date, instrument_id, names, categories, str_of_prices, total))
            db.commit()
            session["cart"] = {} #order made, clear the cart
            return render_template("order.html", message=message, total=total, discount=discount, shipping=shipping, before_discount=before_discount, before_shipping=before_shipping)
    
    #display the cart
    images = {}
    names = {}
    prices = {}
    total = 0
    for instrument_id in session["cart"]:
        db = get_db()
        instrument = db.execute("""SELECT * FROM instruments WHERE instrument_id =  ?;""", (instrument_id,)).fetchone()
        db.commit()
        image = instrument["image"]
        images[instrument_id] = image
        name = instrument["name"]
        names[instrument_id] = name
        price = instrument["price"]
        prices[instrument_id] = price
        total = total + float(prices[instrument_id])
    total = round(total,2)
    return render_template("checkout.html", cart=session["cart"], name=names, price=prices, total=total, image=images, form=form)

@app.route("/remove_order_page", methods=["GET","POST"])
@login_required
def remove_order_page():
    db = get_db()
    orders = db.execute("""SELECT * FROM orders;""").fetchall()
    db.commit()
    return render_template("remove_order_page.html", orders=orders)

@app.route("/remove_order/<int:order_no>")
@login_required
def remove_order(order_no):
    db = get_db()
    db.execute("""DELETE FROM orders WHERE order_no =  ?;""", (order_no,)).fetchone()
    db.commit()
    return redirect( url_for("user_account"))

@app.route("/admin_remove_order/<int:order_no>")
@login_required
def admin_remove_order(order_no):
    db = get_db()
    db.execute("""DELETE FROM orders WHERE order_no =  ?;""", (order_no,)).fetchone()
    db.commit()
    return redirect( url_for("remove_order_page"))

@app.route("/admin_remove_product/<int:instrument_id>")
@login_required
def admin_remove_product(instrument_id):
    db = get_db()
    db.execute("""DELETE FROM instruments WHERE instrument_id =  ?;""", (instrument_id,)).fetchone()
    db.commit()
    return redirect( url_for("remove_instrument"))
    
@app.route("/user_account", methods=["GET","POST"])
@login_required
def user_account():
    
    if session['user_id']:
        user_id = session['user_id']
        db = get_db()
        orders = db.execute("""SELECT * FROM orders WHERE user_id =  ?;""", (user_id,)).fetchall()
        return render_template("user_account.html", orders=orders)
    else:
        return redirect(url_for("index"))

@app.route("/confirmation")
@login_required
def confirmation():
    return render_template("confirmation.html")

@app.route("/remove_account")
@login_required
def remove_account():
    user_id = session['user_id']
    db = get_db()
    db.execute("""DELETE FROM users WHERE user_id =  ?;""", (user_id,)).fetchone()
    db.commit()
    session.clear()
    return redirect( url_for("index"))