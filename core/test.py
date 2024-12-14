from django.test import TestCase

class HomePageTest(TestCase):
    def test_home_page_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_home_page_contains_hello_world(self):
        response = self.client.get('/')
        self.assertContains(response, "Hello, world!")