#!/usr/bin/env python3
'''
Flask web application for i18n projects
'''
from flask import Flask, render_template, request
from flask_babel import Babel


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


@babel.localeselector
def get_locale() -> str:
    '''
    Function that determines the best match with our supported languages
    '''
    if 'locale' in request.args:
        requested_lang = request.args.get('locale')
        if requested_lang in app.config['LANGUAGES']:
            return requested_lang
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/', strict_slashes=False)
def index():
    '''
    Index file that renders the index template
    '''
    return (render_template('4-index.html'))


if __name__ == '__main__':
    '''
    Main function that runs app on port 5000
    '''
    app.run(host='0.0.0.0', port=5000)
