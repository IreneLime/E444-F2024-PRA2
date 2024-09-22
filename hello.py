from flask import Flask, render_template, session, redirect, url_for, flash
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


# Name submission
class NameForm(FlaskForm):
    name = StringField("What is your name?", validators=[DataRequired()])
    submit = SubmitField("Submit")


app = Flask(__name__)
app.config["SECRET_KEY"] = "hard to guess string"
Bootstrap(app)
Moment(app)


# Handle GET and POST requests (form submission)
@app.route("/", methods=["GET", "POST"])
def index():
    form = NameForm()
    if form.validate_on_submit():
        old = session.get("name")
        if old != None and old != form.name.data:
            flash("You have changed your name.")
        session["name"] = form.name.data
        return redirect(url_for("index"))
    return render_template("index.html", form=form, name=session.get("name"))


@app.route("/user/<name>")
def user(name):
    return render_template("user.html", name=name)


if __name__ == "__main__":
    app.run(debug=True)
