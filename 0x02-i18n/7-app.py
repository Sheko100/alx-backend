#!/usr/bin/env python3
"""Module that defines a root route
"""

from flask import Flask, render_template, request, g
from flask_babel import Babel
import pytz

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


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
    user = g.get('user')
    args = request.args
    if 'locale' in request.args and args['locale'] in lang:
        return args['locale']
    elif user and user['locale'] in lang:
        return user['locale']
    return request.accept_languages.best_match(lang)


@babel.timezoneselector
def get_timezone():
    """Gets the timezone
    """
    timezone = ''
    user = g.get('user')
    user_tz = 
    if 'timezone' in request.args:
        timezone = args['locale']
    elif user and user['timezone']:
        timezone = user['timezonq']

    try:
        timezone = pytz.timezone(timezone)
        return timezone
    except pytz.exceptions.UnknownTimeZoneError:
        return app['BABEL_DEFAULT_TIMEZONE']


def get_user():
    """Gets a user info
    """
    user_id = request.args.get('login_as')
    if user_id and int(user_id) in users:
        return users[int(user_id)]
    return None


@app.before_request
def before_request():
    """Assigns a user globally in the app
    """
    user = get_user()
    if user:
        g.setdefault('user', user)


@app.route('/')
def root():
    """ root route
    """
    return render_template('5-index.html')
