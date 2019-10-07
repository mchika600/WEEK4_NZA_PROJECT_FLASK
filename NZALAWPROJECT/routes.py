from NZALAWPROJECT import app, db
from flask import render_template, request, flash, redirect, url_for
# Import of Forms
from NZALAWPROJECT.forms import SignUpForm, SignInForm, ContactForm

# Import Models
from NZALAWPROJECT.models import User, Contact, check_password_hash

# Imports Flask-Login Module/functions
from flask_login import login_user, current_user, logout_user, login_required

# Home Route
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/sign_up",methods=["Get", "POST"])
def sign_up():
    form = SignUpForm()
    if request.method == "POST" and form.validate():
        flash("Thanks for Signing Up!")
        # Gathering Form Data
        username = form.username.data
        email = form.email.data
        password = form.password.data
        print(username, email, password)

        # Add Form Data to User Model Class
        user = User(username, email, password)
        db.session.add(user) # Start communication with Database
        db.session.commit() # Will save data to Database
        return redirect(url_for('sign_in'))

    else:
        flash("Your form is missing some data!")
    return render_template('sign_up.html', sign_up_form=form)

@app.route('/sign_in',methods=["GET","POST"])
def sign_in():
    form = SignInForm()
    if request.method == "POST":
        user_email = form.email.data
        password = form.password.data
        logged_user = User.query.filter(User.email == user_email).first()
        if logged_user and check_password_hash(logged_user.password,password):
            login_user(logged_user)
            print(current_user.username)
            return redirect(url_for('index'))
    return render_template('sign_in.html',sign_in_form = form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/contact', methods = ["GET", "POST"])
def contact():
    form = ContactForm()
    if request.method == "POST":
        name = form.name.data
        email = form.email.data
        phone = form.phone.data
        message = form.message.data
        # Instatiate Contact Class
        contact = Contact(name = name, phone = phone, email = email, message = message)
        db.session.add(contact)
        db.session.commit()

    return render_template('contact.html', contact_form=form)
