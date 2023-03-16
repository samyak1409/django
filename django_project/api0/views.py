from django.http import JsonResponse


# Create your views here.


def get_endpoints(request):
    endpoints = {'Get all Posts': 'GET /posts/',
                 'Get a single Post': 'GET /post/:id/',
                 'Get all Posts by a particular User': 'GET /posts/:username/'}
    return JsonResponse(data=endpoints)
