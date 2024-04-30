from flask import Blueprint, request, jsonify

data = Blueprint('data', __name__)

@data.route('/postdata', methods=['POST'])
def post_data():
    """
    Process the incoming JSON data and return it as a JSON response.

    Returns:
        A JSON response containing the processed data.
    """
    content = request.json
    return jsonify(content)

@data.route('/getjson')
def get_json():
    """
    Returns a JSON object containing a key-value pair and a list of numbers.

    Returns:
        dict: A JSON object with the following structure:
            {
                'key': 'value',
                'numbers': [1, 2, 3]
            }
    """
    return jsonify({'key': 'value', 'numbers': [1, 2, 3]})
