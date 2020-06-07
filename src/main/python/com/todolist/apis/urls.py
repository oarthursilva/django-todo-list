from apis.service import lists
from django.conf.urls import url

urlpatterns = [
    url(r'^lists/(\d+)/$', lists.by_id, name='api_list'),
]
