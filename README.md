-  [Readme](#readme)
   -  [How to configure the enviroment for the project](#how-to-configure-the-enviroment-for-the-project)
   -  [How to run the project](#how-to-run-the-project)
   -  [Structure of the project](#structure-of-the-project)
   -  [BACKLOG](#backlog)
      -  [Frontend](#frontend)
         -  [Components](#components)
         -  [Pages](#pages)
      -  [Backend](#backend)
   -  [FAQ](#faq)
      -  [I want to change how something is displayed in the webpage!](#i-want-to-change-how-something-is-displayed-in-the-webpage)
      -  [How does the `templates/` directory work?](#how-does-the-templates-directory-work)
      -  [How does the static/css folder work?](#how-does-the-staticcss-folder-work)
         -  [File specific files:](#file-specific-files)
         -  [General usage files](#general-usage-files)
      -  [What is inside `datasets/`?](#what-is-inside-datasets)
      -  [How are the sponsors displayed?](#how-are-the-sponsors-displayed)
      -  [How can I modify the FAQ in the homepage?](#how-can-i-modify-the-faq-in-the-homepage)
      -  [How does the logger work?](#how-does-the-logger-work)
      -  [How to use the logger inside the classes/ folder](#how-to-use-the-logger-inside-the-classes-folder)
      -  [What logs do i have? How do them work?](#what-logs-do-i-have-how-do-them-work)
      -  [Whats the purpose of the classes inside classes/ ?](#whats-the-purpose-of-the-classes-inside-classes-)
      -  [What is babel / How does translation work / Why do i see a lot of underscores \_() everywhere / How do i change translation/language?](#what-is-babel--how-does-translation-work--why-do-i-see-a-lot-of-underscores-_-everywhere--how-do-i-change-translationlanguage)
      -  [How are categories translated in sponsors_generator?](#how-are-categories-translated-in-sponsors_generator)
      -  [How do i build the project](#how-do-i-build-the-project)
   -  [Helpful information](#helpful-information)
      -  [helpful links](#helpful-links)
      -  [recommended settings for `settings.json` in Visual Studio Code](#recommended-settings-for-settingsjson-in-visual-studio-code)

# Readme

This is the repository for Nerdearla, the Sysarmy event

## How to configure the enviroment for the project

1. Create a virtual enviroment in a folder called `.venv/` running `python -m venv .venv/`
2. Source that virtual enviroment with `source .venv/bin/activate`, or `source .venv/Scripts/activate` if you are in windows. If you are using powershell, replace / with \
3. Install the packages in `requirements.txt` running `pip install -r requirements.txt`

## How to run the project

1. Source the python virtual enviroment with `source .venv/bin/active`
2. Run flask with `flask run`
3. Enjoy

## Structure of the project

```python
.
└── app: # the files used for the webapp
    ├── static # static files (the css, the fonts, the images and the javascript files)
    │   ├── css # styling
    │   ├── fonts # fonts that are not in Google Fonts
    │   ├── img # images
    │   └── js # javascript code
    └── templates # jinja-html code
			└── components # jinja-html components
```

## BACKLOG

### Frontend

#### Components

-  [x] Navbar
   -  [x] Basic structure and operation
   -  [x] Responsiveness
   -  [x] Final styling
-  [x] Hero
   -  [x] Basic structure and operation
   -  [x] Responsiveness
   -  [x] Final styling
-  [x] About
   -  [x] Basic structure and operation
   -  [x] Responsiveness
   -  [x] Final styling
-  [x] Countdown
   -  [x] Basic structure and operation
   -  [x] Responsiveness
   -  [x] Final styling
-  [x] Nerdearla in numbers (statistics)
   -  [x] Basic structure and operation
   -  [x] Responsiveness
   -  [x] Final styling
-  [ ] Speakers
   -  [ ] Basic structure and operation
   -  [ ] Responsiveness
   -  [ ] Final styling
-  [x] Ubication
   -  [x] Basic structure and operation
   -  [x] Responsiveness
   -  [x] Final styling
-  [x] FAQ
   -  [x] Basic structure and operation
   -  [x] Responsiveness
   -  [x] Final styling
-  [x] Contact
   -  [x] Basic structure and operation
   -  [x] Responsiveness
   -  [x] Final styling
-  [x] Footer
   -  [x] Basic structure and operation
   -  [x] Responsiveness
   -  [x] Final styling

#### Pages

-  [x] Index
   -  [x] Basic structure and operation
   -  [x] Responsiveness
   -  [x] Final styling
-  [x] Sponsors
   -  [x] Basic structure and operation
   -  [x] Responsiveness
   -  [x] Final styling
-  [x] Code of Conduct
   -  [x] Basic structure and operation
   -  [x] Responsiveness
   -  [x] Final styling
-  [ ] Agenda
   -  [x] Basic structure and operation
   -  [ ] Responsiveness
   -  [ ] Final styling
-  [ ] Error pages
   -  [ ] 404 page

### Backend

-  [x] Logging
-  [x] Error handling
   -  [x] routes.py
   -  [x] filters.py
-  [x] Multilanguage support
   -  [x] en
   -  [x] es

## FAQ

### I want to change how something is displayed in the webpage!

First, try to look which component defines that part of the webpage (if you dont know how that works, see the **"How does the `templates/` directory work?"** section).

Next, try to identify if what you are trying to modify is related to **the data that is shown** (backend related, probably inside routes.py),
or **how the data is shown** (frontend related, probably inside your component or a .html file isnide templates/)

If the problem is backend related, try to look for the route that renders the template you are looking at.
For example, if you want to change how data is collected at the sponsors page, look for the definition of the `sponsors/` route

### How does the `templates/` directory work?

Every file inside `templates/` (except `base.html`) is rendered using render_template in an specific route defined in `routes.py`.
Each file inherits from `base.html`, and uses the components in `components/` using `{% include "components/component_name_here.html" %}`

**This is done for the purpose of clean and tidy code**

An example of a component could be:

```html
<!-- This file holds the section that talks about the speakers -->
<section id="speakers">
	<!-- Get the css file using jinja-html syntax -->
	<link rel="stylesheet" href="{{ url_for('static', filename='css/speakers.css') }}" />

	<!-- Main content of the html -->
	<div class="container">
		<h1>Nuestros speakers</h1>
		<div>
			<p>Our speakers are great because...</p>
		</div>
	</div>

	<!-- Get the javascript file using jinja-html syntax -->
	<script src="{{ url_for('static', filename='js/speakers.js') }}"></script>
</section>
```

### How does the static/css folder work?

The CSS folder has two types of .css files

#### File specific files:

Some css files are asociated to html files inside templates/ (or templates/components).
For example, `hero.css` is used in the `hero.html` component, or `sponsors.css` is used in `sponsors.html`

#### General usage files

Other files are for general usage, like `style.css`, which defines general css to be used in the whole project.

-  `fonts.css` loads the fonts from static/fonts/
-  `trama_backgrounds.css` defines classes for generating backgrounds using the tramas inside img/svg/tramas
-  `variables.css` defines global variables, for example the Nerderla colors.

### What is inside `datasets/`?

Datasets is a folder which contains files that modify what and how data is displayed in the page.
**The purpose of this folder was to hold files that modify the webpage without needing to touch the code**

For example, the `sponsors_config.json` file sets the order in which the sponsors are displayed in `sponsors.html`, among other things.
This json file is accessed using `read_json_file()` from `functions.py`
The sponsors are defined inside `sponsors.csv`

### How are the sponsors displayed?

The sponsors are defined in `datasets/sponsors.csv`
`sponsors.csv` should look like this:

```csv
name                  ,category   ,file            ,link
cognizant             ,diamond    ,cognizant.png   ,https://sysar.my/cognizantsoftvision
icbc                  ,adamantium ,icbc.png        ,https://www.icbc.com.ar
openqube              ,adamantium ,openqube.png    ,https://openqube.io/
google cloud platform ,adamantium ,googlecloud.png ,https://cloud.google.com/
rappi                 ,silver     ,rappi.png       ,https://rappi.io/
rappi                 ,silver     ,rappi.png       ,https://rappi.io/
rappi                 ,silver     ,rappi.png       ,https://rappi.io/
```

You can use whitespaces because the `sponsors/` route automatically removes trailing whitespaces

### How can I modify the FAQ in the homepage?

In the `datasets/` folder, create or modify a `faq.json` file with FAQ's like the following:

```json
[
	{
		"title": "Que es Nerdearla",
		"description": "Nerdearla es lorem ipsum bla bla bla"
	},
	{
		"title": "Cuando se hace la Nerdearla",
		"description": "La respuesta esta en tu corazon"
	},
	{
		"title": "Cúanto sale?",
		"description": "Paga Jolo"
	}
]
```

### How does the logger work?

Generated by chatGPT:
To use the logger in each file of your Flask project, you can follow these steps:

1. Create a separate file to configure the logger. Let's call it `logger_config.py`.

```python
import os
import logging
from flask import Flask


def configure_logger(app: Flask):
    """
    Configure and return a logger instance with different handlers for console, Werkzeug logs,
    general logs, and error logs.

    This function sets up a logger with multiple handlers to direct log messages based on their
    level and source. Non-Werkzeug log messages at INFO level and higher are sent to the console
    and written to the 'general.log' file. Only Werkzeug logs are written to the 'werkzeug.log' file.
    ERROR and higher level non-Werkzeug messages are captured in the 'errors.log' file.

    Args:
        app (Flask): The Flask application object.

    Returns:
        logging.Logger: The configured logger instance.

    Note:
        Make sure to call this function after creating the Flask application object.
    """
    # Create a logger instance
    logger = app.logger

    # Set the log level for the logger
    logger.setLevel(logging.DEBUG)

    # Remove existing console handler if present
    for handler in logger.handlers:
        if isinstance(handler, logging.StreamHandler):
            logger.removeHandler(handler)

    # Create a console handler for non-Werkzeug logs
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)
    console_formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
    console_handler.setFormatter(console_formatter)
    logger.addHandler(console_handler)

    # Create the 'logs/' folder if it doesn't exist
    if not os.path.exists("logs/"):
        try:
            os.makedirs("logs/")
        except PermissionError:
            logger.error("Failed to create 'logs/' folder. Check permissions.")

    # Create a file handler for Werkzeug logs
    try:
        werkzeug_handler = logging.FileHandler("logs/werkzeug.log")
        werkzeug_handler.setLevel(logging.DEBUG)  # Set the desired level for Werkzeug logs
        werkzeug_formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
        werkzeug_handler.setFormatter(werkzeug_formatter)
        werkzeug_logger = logging.getLogger("werkzeug")
        werkzeug_logger.setLevel(logging.DEBUG)  # Set the desired level for Werkzeug logs
        werkzeug_logger.addHandler(werkzeug_handler)
    except PermissionError:
        logger.error("Failed to create 'werkzeug.log' file. Check permissions.")

    # Create a file handler for general logs (INFO and higher, excluding Werkzeug and ERROR level)
    try:
        general_handler = logging.FileHandler("logs/general.log")
        general_handler.setLevel(logging.INFO)
        general_formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
        general_handler.setFormatter(general_formatter)
        logger.addHandler(general_handler)
    except PermissionError:
        logger.error("Failed to create 'general.log' file. Check permissions.")

    # Create a file handler for error logs (ERROR and higher, excluding Werkzeug)
    try:
        error_handler = logging.FileHandler("logs/errors.log")
        error_handler.setLevel(logging.ERROR)
        error_formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
        error_handler.setFormatter(error_formatter)
        error_logger = logging.getLogger("errors")
        error_logger.setLevel(logging.ERROR)  # Set the desired level for error logs
        error_logger.addHandler(error_handler)
    except PermissionError:
        logger.error("Failed to create 'errors.log' file. Check permissions.")

    return logger

```

2. In the `__init__.py` file of your app folder, import the `configure_logger` function from `logger_config` and call it, passing the app object.

```python

from flask import Flask
from logger_config import configure_logger

app = Flask(__name__)

# Configure the logger
configure_logger(app)

# Import routes and functions
from app import routes
from app import functions
```

3. In the other files within the app folder (`routes.py`) import the logger and use it as needed.

For example, in `routes.py`:

```python

from flask import request
from app import app

logger = app.logger

@app.route('/')
def index():
    logger.info('Processing index request...')
    # Your code here

```

By importing the app object and logger instance from `__init__.py` in each file, you can access and use the logger across different modules and files within your Flask project.

### How to use the logger inside the classes/ folder

Generated by chatGPT

To use the app logger in the classes located within the classes folder of your Flask project, you can follow these steps:

1. In the `__init__.py` file located inside the classes folder, import the logger from the `__init__.py` file of the app folder.

```python

from app import app

logger = app.logger
```

2. In the other Python files within the classes folder (`DatasetsUtils.py` and `SponsorProcessor.py`), import the logger and use it as needed.

For example, in `DatasetsUtils.py`:

```python

from classes import logger

class DatasetsUtils:
    def some_method(self):
        logger.info('This is an info message from DatasetsUtils')
        # Your code here
```

And in `SponsorProcessor.py`:

```python

from classes import logger

class SponsorProcessor:
    def some_method(self):
        logger.debug('This is a debug message from SponsorProcessor')
        # Your code here
```

By importing the logger from the app module's `__init__.py` file in the `__init__.py` file of the classes folder, you can access and use the app logger across the classes within the classes folder.

### What logs do i have? How do them work?

-  Non-Werkzeug log messages at INFO level and higher are sent to the console
   and written to the 'general.log' file.
-  ERROR and higher level non-Werkzeug messages are captured in the 'errors.log' file.
-  Werkzeug-only logs are written to the 'werkzeug.log' file.

### Whats the purpose of the classes inside classes/ ?

The idea is to divide the code to make it cleaner and easier to use

### What is babel / How does translation work / Why do i see a lot of underscores \_() everywhere / How do i change translation/language?

Its flask babel https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-xiii-i18n-and-l10n

The tutorial shows you how to do scripts integrated with flask, but i hadnt read that part at the moment of creating this scripts

When you replace all text in html files with `{{ _('') }}`,

1. run `sh scripts/extract_messages.sh` (if its not running, run `chmod +x extract_messages.sh` to give it permissions to run).

2. **FIRST TIME** run `sh scripts/generate_language_catalog.sh en`. Replace `en` with the language code you want. In this project, we are translating to english, so we use en.
   If you get a "Please provide a language parameter." error, you forgot to pass the language as a parameter, so it means you forgot the `en` when running the file.

3. After the first time, use `scripts/update_language_catalog.sh` instead of `scripts/generate_language_catalog.sh`

4. Use chatGPT to fill the messages.po file or do it by hand

5. Run `scripts/generate_language_output.sh`

6. Stop flask from running and run it again. Flask does not seem to notice when the messages.po file changes, so you wont see the changes until you reload the server.

### How are categories translated in sponsors_generator?

Its currently hardcoded like this into sponsors_generator.html

Remember that categories are automatically converted into lowercase when retrieved from the csv

```
{# HACK: This hardcoded thing here translates special categories titles into other languages #}
{% if lang_code == "en" %}
	{# HACK: The special categories are here #}
	{% if category == "nos apoyan" %}
		{% set category = "supported by" %}
	{% endif %}
	{% if category == "comunidades" %}
		{% set category = "communities" %}
	{% endif %}
{% endif %}

<h1> {{category}} </h1>
```

### How do i build the project

1. Run python freeze.py

## Helpful information

### helpful links

Understanding Flask: https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world **(READ FIRST)**

Understanding multilanguage: https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-xiii-i18n-and-l10n and https://medium.com/@nicolas_84494/flask-create-a-multilingual-web-application-with-language-specific-urls-5d994344f5fd

Jinja formatter: https://stackoverflow.com/questions/60175608/visual-studio-code-and-jinja-templates

Using Flask, Flask-WTF, and AJAX for forms:
If you are confused about how contact.html, submit_contact/ and contact.js work, watch this video: https://www.youtube.com/watch?v=QKcVjdLEX_s and then read this blog https://blog.carsonevans.ca/2019/08/20/validating-ajax-requests-with-wtforms-in-flask/

Understanding logging:
https://www.youtube.com/watch?v=-ARI4Cz-awo and https://www.youtube.com/watch?v=jxmzY9soFXg

### recommended settings for `settings.json` in Visual Studio Code

You should add this line in your User settings.json.
The reason for that is because that specific line is not available for workspace specific configuration, which is defined in the `.vscode/settings.json` file

```json
{
	"css.enabledLanguages": ["jinja-html", "django-html", "html"]
}
```
