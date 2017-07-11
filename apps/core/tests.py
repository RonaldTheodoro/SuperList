from django.test import TestCase
from .views import index


class HomePageTest(TestCase):

    def test_home_page_returns_correts_html(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'index.html')

    def test_uses_home_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'index.html')

    def test_can_save_a_POST_request(self):
        response = self.client.post('/', data={'item_text': 'A new list item'})
        self.assertIn('A new list item', response.content.decode())
        self.assertTemplateUsed(response, 'index.html')
