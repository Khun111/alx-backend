#!/usr/bin/env python3
'''Basic flask app'''
from flask import Flask, render_template, request
from flask_babel import Babel
app = Flask(__name__)
babel = Babel(app)


class Config:
    '''Config class for babel settings'''
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


@babel.localeselector
def get_locale():
    '''Function for setting locale'''
    return request.accept_languages.best_match(app.config["LANGUAGES"])


app.config.from_object(Config)


@app.route('/')
def home():
    '''Index page view'''
    return render_template('2-index.html')


if __name__ == '__main__':
    app.run(debug=True)
