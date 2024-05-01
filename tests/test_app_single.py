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

if __name__ == '__main__':
    unittest.main()
