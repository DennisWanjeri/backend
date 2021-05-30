#!/usr/bin/env python3
"""
Babel Flask extension
"""


from flask import Flask, render_template, request, g
from flask_babel import Babel
import pytz

app = Flask(__name__)
babel = Babel(app)


class Config:
    """configuration module"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}

def get_user():
    """
    get user
    """
    user_id = request.args.get('login_as')
    if user_id:
        try:
            return users[int(user_id)]
        except Exception:
            return None
    return None


@app.before_request
def before_request():
    """
    before request
    """
    g.user = get_user()
    


@babel.localeselector
def get_locale():
    """
    get_locale
    """
    locale = request.args.get("locale")
    if locale and locale in Config.LANGUAGES:
        return locale
    user = request.args.get("login_as")
    if user:
        lang = users.get(int(user)).get('locale')
        if lang in Config.LANGUAGES:
            return lang
    headers = request.headers.get("locale")
    if headers:
        return headers
    return request.accept_languages.best_match(Config.LANGUAGES)
@babel.timezoneselector
def get_timezone():
    """
    get_timezone
    """
    timezone = request.args.get('timezone')
    if timezone:
        try:
            return pytz.timezone(timezone)
        except pytz.exceptions.UnknownTimeZoneError:
            pass
    if g.user:
        timezone = g.user.get('timezone')
        if timezone:
            try:
                return pytz.timezone(timezone)
            except pytz.exceptions.UnknownTimeZoneError:
                pass
    return pytz.timezone('utc')
    

@app.route('/', methods=["GET"], strict_slashes=False)
def hello():
    """
    hello.
    """
    return render_template('6-index.html', user=g.user)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
