from unittest import *
from app import create_app

class TestHomeRoute(TestCase):
    def setUp(self):
        self.app = create_app().test_client()

    def test_homeRoute(self):
        rv = self.app.get('/api/')
        self.assertEqual({"message": 'Hello World!'}, rv.get_json())

if __name__ == '__main__':
    main()


