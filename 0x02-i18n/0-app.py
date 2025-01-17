#!/usr/bin/python3
"""Module that defines a root route
"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def root():
    """ root route
    """
    return render_template('0-index.html')
