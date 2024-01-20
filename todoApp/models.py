# todo_app/models.py
from django.db import models

class ToDoList(models.Model):
    title = models.CharField(max_length=200)

class ToDo(models.Model):
    task = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)
    task_list = models.ForeignKey(ToDoList, on_delete=models.CASCADE)
