# Create your views here.
from django.http import HttpResponse


def main_view(request):
    return HttpResponse('<html><title>To-Do lists</title></html>')
