"""
The filters.py file is responsible for defining custom Jinja filters used in the Flask project.
Jinja filters allow modifying or formatting data within templates.
"""
from app import app


@app.template_filter("whitespace_to_dash")
def whitespace_to_dash_filter(text):
    """
    Custom Jinja filter to replace whitespaces with dashes in a text.
    Usage:

    To use this custom filter in a template, you can apply it using
    the | operator and the filter name, whitespace_to_dash.
    For example:
    {{ my_text|whitespace_to_dash }}

    Args:
        text (str): The input text.

    Returns:
        str: The text with whitespaces replaced by dashes.
    """
    if not isinstance(text, str):
        raise TypeError("Input must be a string.")
    return text.replace(" ", "-")
