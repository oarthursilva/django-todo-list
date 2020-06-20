from django.http import HttpResponse


def by_id(request, list_id):
    return HttpResponse(content_type='application/json')
