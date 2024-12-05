# from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.

def hello_world(request, name_from_path=None):
    name = request.GET.get('name', 'Unknown Person')

    return JsonResponse({"message": f"Hello, {name}!",
                         "name_from_path": name_from_path})
# http://127.0.0.1:8000/hello?name=Josh