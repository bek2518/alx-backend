#!/usr/bin/env python3
'''
Flask web application for i18n projects
'''
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    '''
    Index file that renders the index template
    '''
    return (render_template('0-index.html'))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
