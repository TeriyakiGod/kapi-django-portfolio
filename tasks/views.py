from django.shortcuts import render, redirect
from .models import Task

def list(request):
    tasks = Task.objects.all()
    return render(request, 'tasks/list.html', {'tasks': tasks})

def detail(request, task_id):
    task = Task.objects.get(id=task_id)
    return render(request, 'tasks/detail.html', {'task': task})

def create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        task = Task(title=title, description=description)
        task.save()
        return redirect('tasks:list')
    return render(request, 'tasks/create.html')

def update(request, task_id):
    task = Task.objects.get(id=task_id)
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        task.title = title
        task.description = description
        task.save()
        return redirect('tasks:list')
    return render(request, 'tasks/update.html', {'task': task})

def delete(request, task_id):
    task = Task.objects.get(id=task_id)
    task.delete()
    return redirect('tasks:list')

