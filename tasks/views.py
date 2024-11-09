from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

def list(request):
    tasks = Task.objects.all()
    return render(request, 'tasks/list.html', {'tasks': tasks})

def detail(request, id):
    task = Task.objects.get(id=id)
    return render(request, 'tasks/detail.html', {'task': task})

def create(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tasks:index')
    else:
        form = TaskForm()
    return render(request, 'tasks/create.html', {'form': form})

def update(request, id):
    task = Task.objects.get(id=id)
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        task.title = title
        task.description = description
        task.save()
        return redirect('tasks:index')
    return render(request, 'tasks/update.html', {'task': task})

def delete(request, id):
    task = Task.objects.get(id=id)
    task.delete()
    return redirect('tasks:index')

@csrf_exempt
def toggle_task_status(request, id):
    if request.method == 'POST':
        task = Task.objects.get(id=id)
        task.completed = not task.completed
        task.save()
        return JsonResponse({'completed': task.completed})