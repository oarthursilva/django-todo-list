# unit test test the application from the inside
from django.test import TestCase
from django.urls import resolve

from lists.views import main_view


class MainViewTest(TestCase):

    def test_should_resolve_root_url_when_main_view_is_requested(self):
        found = resolve("/")
        self.assertEquals(found.func, main_view)

    def test_should_return_valid_html_when_main_view_is_requested(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'main.html')

    def test_should_save_new_item_when_post_is_triggered(self):
        response = self.client.post('/', data={'item_text': 'A new list item'})
        self.assertIn('A new list item', response.content.decode())
        self.assertTemplateUsed(response, 'main.html')
