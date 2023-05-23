#!/usr/bin/env python3
'''
Flask web application for i18n projects
'''
from flask import Flask, render_template, request, g
from flask_babel import Babel, _
import pytz


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


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
def get_locale():
    '''
    Function that determines the best match with our supported languages
    '''
    if 'locale' in request.args:
        requested_lang = request.args.get('locale')
        if requested_lang in app.config['LANGUAGES']:
            return requested_lang

    if g.user:
        if g.user['locale'] in app.config['LANGUAGES']:
            return g.user['locale']

    if 'locale' in request.headers:
        requested_lang = request.headers.get('locale')
        if requested_lang in app.config['LANGUAGES']:
            return requested_lang
    return request.accept_languages.best_match(app.config['LANGUAGES'])


def get_user():
    '''
    Function that returns a user dictionary if login_as passed
    or None if not
    '''
    if 'login_as' in request.args:
        user_id = int(request.args.get('login_as'))
        if user_id in users.keys():
            user = users[user_id]
            return user
        return None
    return None


@app.before_request
def before_request():
    '''
    Function that runs before all other functions which uses get_user
    to find a user if any, and set it as a global on flask.g.user
    '''
    user = get_user()
    g.user = user


@babel.timezoneselector
def get_timezone():
    '''
    Function that finds timezone parameter based on criteria
    '''
    if 'timezone' in request.args:
        requested_timezone = request.args.get('timezone')
        try:
            pytz.timezone(requested_timezone)
            return requested_timezone
        
        except pytz.exceptions.UnknownTimeZoneError:
            return app.config['BABEL_DEFAULT_TIMEZONE']

    if g.user:
        try:
            pytz.timezone(g.user['timezone'])
            return g.user['timezone']
        
        except pytz.exceptions.UnknownTimeZoneError:
            return app.config['BABEL_DEFAULT_TIMEZONE']


@app.route('/', strict_slashes=False)
def index():
    '''
    Index file that renders the index template
    '''
    return (render_template('7-index.html'))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
