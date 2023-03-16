from rest_framework.decorators import api_view
from rest_framework.response import Response


# Create your views here.


@api_view(http_method_names=['GET'])
def available_endpoints(request):
    endpoints = {'Get all Posts': 'GET /posts/',
                 'Get a single Post': 'GET /post/:id/',
                 'Get all Posts by a particular User': 'GET /posts/:username/'}
    return Response(data=endpoints)
