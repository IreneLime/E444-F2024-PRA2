from flask import Flask, render_template, session, redirect, url_for, flash
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


# User Info submission
class UserForm(FlaskForm):
    name = StringField("What is your name?", validators=[DataRequired()])
    email = StringField("What is your UofT email address?", validators=[DataRequired()])
    submit = SubmitField("Submit")


app = Flask(__name__)
app.config["SECRET_KEY"] = "hard to guess string"
Bootstrap(app)
Moment(app)


# Handle GET and POST requests (form submission)
@app.route("/", methods=["GET", "POST"])
def index():
    form = UserForm()
    if form.validate_on_submit():
        old = session.get("name")
        # Pop up message if the user changes their name
        if old != None and old != form.name.data:
            flash("You have changed your name.")
        session["name"] = form.name.data

        old_email = session.get("email")
        # Pop up message if the user changes their email
        if old_email != None and old_email != form.email.data:
            flash("You have changed your email.")

        # Check for string "utoronto" in input email
        if "utoronto" not in form.email.data:
            session["message"] = "Please use your UofT email."
        else:
            session["message"] = f"Your UofT email is {form.email.data}"
        session["email"] = form.email.data
        return redirect(url_for("index"))

    return render_template(
        "index.html",
        form=form,
        name=session.get("name"),
        emailMesssage=session.get("message"),
    )


@app.route("/user/<name>")
def user(name):
    return render_template("user.html", name=name)


if __name__ == "__main__":
    app.run(debug=True)
