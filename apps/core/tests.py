from django.test import TestCase
from django.urls import resolve
from django.http import HttpRequest
from .views import index


class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        response = resolve('/')
        self.assertEqual(response.func, index)

    def test_home_page_returns_correts_html(self):
        request = HttpRequest()
        response = index(request)
        html = response.content.decode('utf-8')
        self.assertTrue(html.startswith('<html>'))
        self.assertIn('<title>To-Do lists</title>', html)
        self.assertTrue(html.endswith('</html>'))
