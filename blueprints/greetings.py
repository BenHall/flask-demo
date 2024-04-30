from flask import Blueprint

greetings = Blueprint('greetings', __name__)

@greetings.route('/hello')
def hello():
    """
    Returns a greeting message.

    Returns:
        str: A greeting message.
    """
    return 'Hello there!'

@greetings.route('/goodbye')
def goodbye():
    """
    Returns a string representing a goodbye message.
    """
    return 'Goodbye!'
