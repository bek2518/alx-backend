#!/usr/bin/env python3
'''
Flask web application for i18n projects
'''
from flask import Flask, render_template, request
from flask_babel import Babel, get_timezone, get_locale


class Config(object):
    '''
    Config class that has a LANGUAGES class attribute that is used
    to configure available languages in our app
    '''
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@babel.localselector
def get_locale():
    '''
    Function that determines the best match with our supported languages
    '''
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/', strict_slashes=False)
def index():
    '''
    Index file that renders the index template
    '''
    return (render_template('0-index.html'))
