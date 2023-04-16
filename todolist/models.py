from django.db import models
from django.contrib.auth.models import User


class ToDoList(models.Model):
    def __str__(self):
        return self.user.username
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=150)


class ToDoItem(models.Model):
    def __str__(self):
        return self.task_name
    todolist = models.ForeignKey(ToDoList, on_delete=models.CASCADE)
    task_name = models.CharField(max_length=150, blank=False)
    task_desc = models.CharField(max_length=10000, blank=False)
