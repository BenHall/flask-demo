from flask import Blueprint, request, jsonify

data = Blueprint('data', __name__)

@data.route('/postdata', methods=['POST'])
def post_data():
    content = request.json
    return jsonify(content)

@data.route('/getjson')
def get_json():
    return jsonify({'key': 'value', 'numbers': [1, 2, 3]})
