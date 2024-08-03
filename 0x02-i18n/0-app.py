#!/usr/bin/env python3
"""Module that defines a flask app with root route
"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    """prints Hello World to the root route"""
    return render_template('0-index.html')
