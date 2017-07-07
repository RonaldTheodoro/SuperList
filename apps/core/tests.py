from django.test import TestCase
from django.urls import resolve
from .views import index


class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        response = resolve('/')
        self.assertEqual(response.func, index)