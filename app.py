from flask import Flask
from blueprints.greetings import greetings
from blueprints.data import data

app = Flask(__name__)
app.register_blueprint(greetings)
app.register_blueprint(data)

@app.route('/')
def index():
    """
    This function returns a welcome message for the Flask demo with Blueprints.
    """
    return 'Welcome to the Flask demo with Blueprints!'

if __name__ == '__main__':
    app.run(debug=True)
