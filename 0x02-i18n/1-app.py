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


@app.route('/', strict_slashes=False)
def index():
    '''
    Index file that renders the index template
    '''
    return (render_template('1-index.html'))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
