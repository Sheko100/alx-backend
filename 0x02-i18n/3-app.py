#!/usr/bin/env python3
"""Module that defines a flask app with root route
"""
from flask import Flask, render_template, request
from flask_babel import Babel, gettext


class Config:
    """configuration for babel"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)

app.config.from_object(Config)

babel = Babel(app)


@babel.localeselector
def get_locale():
    """Gets the siutable language for the user"""
    return request.accept_languages.best_match(app.config["LANGUAGES"])


@app.route('/')
def hello_world():
    """prints hello world on the root"""
    return render_template('3-index.html', title=gettext('home_title'), header=gettext('home_header'))

