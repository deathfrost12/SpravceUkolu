from django.shortcuts import render
from django.views.generic import DetailView
from .models import Task

def index(request):
    tasks_ready = Task.objects.filter(status='pending')
    tasks_in_progress = Task.objects.filter(status='in_progress')
    tasks_done = Task.objects.filter(status='completed')
    
    context = {
        'tasks_ready': tasks_ready,
        'tasks_in_progress': tasks_in_progress,
        'tasks_done': tasks_done,
    }
    return render(request, 'index.html', context)

class TaskDetailView(DetailView):
    model = Task
    template_name = 'task_detail.html'
    context_object_name = 'task'
