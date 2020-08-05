from django.test import Client, TestCase
import os


c = Client()


class AppTestCase(TestCase):
    def test_correct_response(self):
        response = c.get('/posts/')
        print(response.status_code)
        self.assertEqual(response.status_code, 200)

    def test_correct_response(self):
        response = c.get('/posts/?order=title&limit=10')
        print(response.status_code)
        self.assertEqual(response.status_code, 200)

    def test_correct_response(self):
        response = c.get('/posts/?order=no_name&limit=-10&offset=900')
        print(response.status_code)
        self.assertEqual(response.status_code, 200)


