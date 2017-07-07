from django.test import TestCase
from .views import index


class HomePageTest(TestCase):

    def test_home_page_returns_correts_html(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'index.html')
