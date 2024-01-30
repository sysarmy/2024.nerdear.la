from flask import Flask, request, session
from .logger_config import configure_logger
from flask_babel import Babel

app = Flask(__name__)

# Configure the logger
configure_logger(app)

# Initialize babel https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-xiii-i18n-and-l10n
babel = Babel(app)
from app import filters
from app import routes

app.config["BABEL_LANGUAGES"] = {
    "en": "English",
    "es": "Español",
}


def get_locale():
    # Use the language code from the URL prefix if available
    lang_code = request.path.split("/")[1]
    if lang_code in app.config["BABEL_LANGUAGES"]:
        return lang_code

    # Fall back to the default locale
    return request.accept_languages.best_match(app.config["BABEL_LANGUAGES"])


babel.init_app(app, locale_selector=get_locale)
