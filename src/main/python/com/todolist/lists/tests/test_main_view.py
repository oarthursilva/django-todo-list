# unit test test the application from the inside
from django.test import TestCase
from lists.models import Item


class MainViewTest(TestCase):

    # def test_should_resolve_root_url_when_main_view_is_requested(self):
    #     found = resolve("/")
    #     self.assertEquals(found.func, main_view)

    def test_should_return_valid_html_when_main_view_is_requested(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'main.html')

    def test_should_not_save_new_item_when_request_is_empty(self):
        self.client.get('/')
        self.assertEqual(0, Item.objects.count())

    def test_should_save_new_item_when_POST_is_triggered(self):
        self.client.post('/', data={'item_text': 'A new list item'})

        self.assertEqual(Item.objects.count(), 1)
        new_item = Item.objects.first()
        self.assertEqual(new_item.text, 'A new list item')

    def test_should_redirect_when_POST_is_triggered(self):
        response = self.client.post('/', data={'item_text': 'A new list item'})

        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['location'], '/')

    def test_should_display_all_items_when_multiple_is_requested(self):
        Item.objects.create(text='item 1')
        Item.objects.create(text='item 2')

        response = self.client.get('/')

        self.assertEqual(Item.objects.count(), 2)
        self.assertIn('item 1', response.content.decode())
        self.assertIn('item 2', response.content.decode())
