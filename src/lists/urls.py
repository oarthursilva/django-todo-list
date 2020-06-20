from django.conf.urls import url
from lists import views as list_view

urlpatterns = [
    url(r'^$', list_view.main, name='main_view')
]
