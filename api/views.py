from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TodoSerializer
from .models import Todo


class TodoView(viewsets.ModelViewSet):
    serializer_class = TodoSerializer
    queryset = Todo.objects.all()


"""
API Overview
"""


@api_view(['GET'])
def Overview(request):
    api_urls = {
        'List': '/list/',
        'Detail View': '/detail/<str:pk>/',
        'Create': '/create/',
        'Update': '/update/<str:pk>/',
        'Delete': '/delete/<str:pk>/',
    }
    return Response(api_urls)


@api_view(['GET'])
def List(request):
    todos = Todo.objects.all()
    serializer = TodoSerializer(todos, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def Detail(request, pk):
    todos = Todo.objects.get(id=pk)
    serializer = TodoSerializer(todos, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def Update(request, pk):
    todo = Todo.objects.get(id=pk)
    serializer = TodoSerializer(instance=todo, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['POST'])
def Create(request):
    serializer = TodoSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def Delete(request, pk):
    task = Todo.objects.get(id=pk)
    task.delete()
    return Response("Todo deleted successfully.")
