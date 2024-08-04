#!/usr/bin/env python3
"""Module that defines a flask app with root route
"""
from flask import Flask, render_template
from flask_babel import Babel


class Config:
    """configuartion for babel"""
    LANGUAGES = ["en", "fr"]


app = Flask(__name__)

app.config.from_object(Config)

babel = Babel(
        app,
        default_locale="en",
        default_timezone="UTC"
        )


@app.route('/')
def hello_world():
    """prints hello world on the root"""
    return render_template('1-index.html')
