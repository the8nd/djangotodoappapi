from django.db import models


class ToDoList(models.Model):
    def __str__(self):
        return self.username
    username = models.CharField(max_length=20)
    description = models.CharField(max_length=150)


class ToDoItem(models.Model):
    def __str__(self):
        return self.task_name
    todolist = models.ForeignKey(ToDoList, on_delete=models.CASCADE)
    task_name = models.CharField(max_length=150, blank=False)
    task_desc = models.CharField(max_length=10000, blank=False)
