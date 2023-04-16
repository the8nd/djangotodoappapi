from rest_framework import viewsets, permissions
from rest_framework.decorators import api_view

from todolist.api.serializers import ToDoItemSerializer, ToDoListSerializer
from todolist.models import ToDoList, ToDoItem


class ToDoListViewSet(viewsets.ModelViewSet):
    queryset = ToDoList.objects.all()
    serializer_class = ToDoListSerializer
    permission_classes = [permissions.IsAuthenticated]


class ToDoItemViewSet(viewsets.ModelViewSet):
    queryset = ToDoItem.objects.all()
    serializer_class = ToDoItemSerializer
    permission_classes = [permissions.IsAuthenticated]

