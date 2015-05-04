"""Tech talk Flask server."""

from flask import Flask, render_template, redirect, flash, session

import jinja2

app = Flask(__name__)

#app.jinja_env.undefined = jinja2.StructureUndefined
"""Tells Jinja to make an error if you refer to an undefined 
    variable in a Jinja template. Helps for debugging."""

@app.route('/')
def say_hello():
    return "hello"

@app.route('/homepage')
def home_page():
    return render_template('homepage.html')

@app.route('/how-to-use')
def how_to_use():
    return render_template('how-to-use.html')

if __name__ == "__main__":
    app.run(debug=True)