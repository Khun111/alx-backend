#!/usr/bin/env python3
'''Basic flask app'''
from flask import Flask, render_template, request, g
from flask_babel import Babel
app = Flask(__name__)
babel = Babel(app)


class Config:
    '''Config class for babel settings'''
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


@babel.localeselector
def get_locale():
    '''Function for setting locale'''
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale
    locale = g.user['locale']
    if locale in app.config['LANGUAGES']:
        return locale
    locale = request.accept_languages.best_match(app.config["LANGUAGES"])
    return locale if locale in app.config['LANGUAGES'] else 'en'


app.config.from_object(Config)


def get_user(user_id):
    '''Function to get user dictionary'''
    return users[user_id]


@app.before_request
def before_request():
    '''Function to get user'''
    user_id = request.args.get('login_as')
    g.user = get_user(int(user_id)) if user_id else None


@app.route('/')
def home():
    '''Index page view'''
    user = g.user['name'] if g.user else None
    return render_template('6-index.html', user=user)


if __name__ == '__main__':
    app.run(debug=True)
