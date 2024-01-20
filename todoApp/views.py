from django.shortcuts import render, redirect
from .models import ToDo, ToDoList

def index(request):
    lists = ToDoList.objects.all()
    return render(request, 'todoApp/index.html', {'lists': lists})

def add_list(request):
    if request.method == "POST":
        title = request.POST['title']
        new_list = ToDoList(title=title)
        new_list.save()
        return redirect('index')
    return render(request, 'todoApp/add_list.html')

def add_task(request, list_id):
    task_list = ToDoList.objects.get(pk=list_id)
    if request.method == "POST":
        task = request.POST['task']
        new_task = ToDo(task=task, task_list=task_list)
        new_task.save()
        return redirect('todoApp:index')
    return render(request, 'todoApp/add_task.html', {'task_list': task_list})

def complete_task(request, task_id):
    task = ToDo.objects.get(pk=task_id)
    task.completed = True
    task.save()
    return redirect('index')
