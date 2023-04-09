from rest_framework import serializers
from todolist.models import ToDoList, ToDoItem


class ToDoListSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ToDoList
        fields = ['username', 'description']


class ToDoItemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ToDoItem
        fields = ['todolist', 'task_name', 'task_desc']
