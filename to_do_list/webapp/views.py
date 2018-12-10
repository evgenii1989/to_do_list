from django.shortcuts import render, redirect, get_object_or_404
from webapp.models import Task


def index_view(request):
    tasks = Task.objects.all()
    context = {
        'tasks': tasks
    }
    return render(request, 'index.html', context)

def create_task_view(request):
    task = Task.objects.create(
        name=request.POST.get('task_name')
    )
    return redirect('tasks')
# Create your views here.
