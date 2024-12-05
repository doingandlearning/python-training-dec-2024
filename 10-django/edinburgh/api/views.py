# from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.viewsets import ModelViewSet
from .models import Book
from .serializers import BookSerializer

class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# Create your views here.

def hello_world(request, name_from_path=None):
    name = request.GET.get('name', 'Unknown Person')

    return JsonResponse({"message": f"Hello, {name}!",
                         "name_from_path": name_from_path})
# http://127.0.0.1:8000/hello?name=Josh

@api_view(["GET", "POST"])
@renderer_classes([JSONRenderer])
def drf_view(request):
    if request.method == "GET":
        return Response({"message": "Hello, for DRF!"})
    elif request.method == "POST":
        return Response({"data": request.body})

