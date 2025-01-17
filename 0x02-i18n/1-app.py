#!/usr/bin/env python3
"""Module that defines a root route
"""

from flask import Flask, render_template
from flask_babel import Babel


class Config:
    """Configuration for i18n
    """
    LANGUAGES = ['en', 'fr']


app = Flask(__name__)
app.config.from_object(Config)
app.config['BABEL_DEFAULT_LOCALE'] = 'en'
app.config['BABEL_DEFAULT_TIMEZONE'] = 'UTC'
babel = Babel(app)


@app.route('/')
def root():
    """ root route
    """
    return render_template('1-index.html')
