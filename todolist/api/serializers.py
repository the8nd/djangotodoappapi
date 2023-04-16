from rest_framework import serializers
from todolist.models import ToDoList, ToDoItem


class ToDoListSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ToDoList
        fields = ['user_id', 'description']


class ToDoItemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ToDoItem
        fields = ['todolist', 'task_name', 'task_desc']
