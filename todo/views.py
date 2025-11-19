from django.shortcuts import render, redirect, get_object_or_404
from .models import Task

def add_task(request):
    if request.method == 'POST':
        task_text = request.POST.get('task')
        if task_text:
            Task.objects.create(task=task_text)
        return redirect('home')
    
    tasks = Task.objects.filter(is_completed=False)
    completed_tasks = Task.objects.filter(is_completed=True)
    
    return render(request, 'home.html', {
        'tasks': tasks,
        'completed_tasks': completed_tasks
    })

def mark_as_done(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.is_completed = True
    task.save()
    return redirect('home')

def mark_as_undone(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.is_completed = False
    task.save()
    return redirect('home')

def delete_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.delete()
    return redirect('home')

def edit_task(request, pk):
    get_task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        task_text = request.POST.get('task')
        if task_text:
            get_task.task = task_text
            get_task.save()
        return redirect('home')
    else:
        contaxt={
            "get_task":get_task
        }
    return render(request, 'edit_task.html',contaxt )