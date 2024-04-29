import unittest
from app import app
from flask import json

class FlaskTestCase(unittest.TestCase):

    def setUp(self):
        # Set up the Flask test client
        self.app = app.test_client()
        # Propagate the exceptions to the test client
        self.app.testing = True

    def test_index(self):
        # Test the index endpoint
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Welcome to the Flask demo with Blueprints!', response.data.decode())

    def test_hello(self):
        # Test the /hello endpoint from greetings blueprint
        response = self.app.get('/hello')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Hello there!', response.data.decode())

    def test_goodbye(self):
        # Test the /goodbye endpoint from greetings blueprint
        response = self.app.get('/goodbye')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Goodbye!', response.data.decode())

    def test_get_json(self):
        # Test the /getjson endpoint
        response = self.app.get('/getjson')
        self.assertEqual(response.status_code, 200)
        # Check that the response is JSON and has the expected content
        self.assertEqual(response.json, {'key': 'value', 'numbers': [1, 2, 3]})

    def test_post_data(self):
        # Test the /postdata endpoint with a POST request
        response = self.app.post('/postdata',
                                 data=json.dumps({'name': 'Jane', 'age': 28}),
                                 content_type='application/json')
        self.assertEqual(response.status_code, 200)
        # Check that the response is JSON and the data matches what was sent
        self.assertEqual(response.json, {'name': 'Jane', 'age': 28})

if __name__ == '__main__':
    unittest.main()
