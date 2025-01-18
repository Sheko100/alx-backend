#!/usr/bin/env python3
"""Module that defines a root route
"""

from flask import Flask, render_template, request
from flask_babel import Babel


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
    lang = app.config['LANGUAGES']
    args = request.args
    if 'locale' in request.args and args['locale'] in lang:
        return args['locale']
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def root():
    """ root route
    """
    return render_template('4-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
