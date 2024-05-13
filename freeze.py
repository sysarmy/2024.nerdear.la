from flask_frozen import Freezer
from app import app
from flask import url_for
from flask_babel import force_locale

# Add base url for https://sysarmy.com/2024.nerdear.la/
# app.config["FREEZER_BASE_URL"] = "/2024.nerdear.la/"

freezer = Freezer(app, log_url_for=False)


@freezer.register_generator
def redirect_index():
    generated_url = url_for("redirect_index")
    print(f"Generated URL: {generated_url}")
    yield generated_url


@freezer.register_generator
def index():
    for lang in ["en", "es"]:
        with force_locale(lang):
            generated_url = url_for("index", lang_code=lang)
            print(f"Generated URL: {generated_url}")
            yield generated_url


@freezer.register_generator
def code_of_conduct():
    for lang in ["en", "es"]:
        with force_locale(lang):
            generated_url = url_for("code_of_conduct", lang_code=lang)
            print(f"Generated URL: {generated_url}")
            yield generated_url


@freezer.register_generator
def sponsors():
    for lang in ["en", "es"]:
        with force_locale(lang):
            generated_url = url_for("sponsors", lang_code=lang)
            print(f"Generated URL: {generated_url}")
            yield generated_url


@freezer.register_generator
def donation():
    for lang in ["en", "es"]:
        with force_locale(lang):
            generated_url = url_for("donation", lang_code=lang)
            print(f"Generated URL: {generated_url}")
            yield generated_url


@freezer.register_generator
def agenda():
    for lang in ["en", "es"]:
        with force_locale(lang):
            generated_url = url_for("agenda", lang_code=lang)
            print(f"Generated URL: {generated_url}")
            yield generated_url


@freezer.register_generator
def uade():
    for lang in ["en", "es"]:
        with force_locale(lang):
            generated_url = url_for("uade_deep_racer", lang_code=lang)
            print(f"Generated URL: {generated_url}")
            yield generated_url

@freezer.register_generator
def captioner():
    for lang in ["en", "es"]:
        with force_locale(lang):
            generated_url = url_for("captioner", lang_code=lang)
            print(f"Generated URL: {generated_url}")
            yield generated_url



@freezer.register_generator
def transcription():
    for lang in ["en", "es"]:
        with force_locale(lang):
            generated_url = url_for("transcription", lang_code=lang)
            print(f"Generated URL: {generated_url}")
            yield generated_url




if __name__ == "__main__":
    freezer.freeze()
