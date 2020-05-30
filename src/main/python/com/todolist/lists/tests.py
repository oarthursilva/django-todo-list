# unit test test the application from the inside

from django.test import TestCase
from django.urls import resolve
from lists.views import main_page


class HomePageTest(TestCase):

    def test_should_root_url_resolve_to_main_view(self):
        found = resolve("/")
        self.assertEquals(found.func, main_page)
