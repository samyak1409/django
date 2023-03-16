from django.http import JsonResponse


# Create your views here.


def available_endpoints(request):
    endpoints = {'Get all Posts': 'GET /posts/',
                 'Get a single Post': 'GET /posts/:id/',
                 'Get all Posts by a particular User': 'GET /posts/by/:username/'}
    return JsonResponse(data=endpoints)
