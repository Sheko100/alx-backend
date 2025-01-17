#!/usr/bin/env python3
"""Module that defines a root route
"""

from flask import Flask, render_template, request
from flask_babel import Babel, gettext as _


class Config:
    """Configuration for i18n
    """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale():
    """ Gets the locale
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def root():
    """ root route
    """
    return render_template('3-index.html')
