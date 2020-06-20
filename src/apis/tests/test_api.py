from apis.models import List
from django.test import TestCase


class ListAPITest(TestCase):
    base_url = '/api/lists/{}'

    def test_api_should_return_OK_when_requested(self):
        _list = List.objects.create()
        response = self.client.get(self.base_url.format(_list._id))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['content-type'], 'application/json')
