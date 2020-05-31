# unit test test the application from the inside
from django.http import HttpRequest
from django.test import TestCase
from django.urls import resolve

from lists.views import main_view


class MainViewTest(TestCase):

    def test_should_resolve_root_url_when_main_view_is_requested(self):
        found = resolve("/")
        self.assertEquals(found.func, main_view)

    def test_should_return_valid_html_when_main_view_is_requested(self):
        request = HttpRequest()
        response = main_view(request)

        html = response.content.decode('utf-8')
        self.assertTrue(html.startswith('<html>'))
        self.assertIn('<title>To-Do lists</title>', html)
        self.assertTrue(html.endswith('</html>'))
