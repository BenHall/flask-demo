from flask import Blueprint

greetings = Blueprint('greetings', __name__)

@greetings.route('/hello')
def hello():
    return 'Hello there!'

@greetings.route('/goodbye')
def goodbye():
    return 'Goodbye!'
