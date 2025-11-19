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

def mark_as_done(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.is_completed = True
    task.save()
    return redirect('home')

def mark_as_undone(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.is_completed = False
    task.save()
    return redirect('home')

def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.delete()
    return redirect('home')

def edit_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == 'POST':
        task_text = request.POST.get('task')
        if task_text:
            task.task = task_text
            task.save()
        return redirect('home')
    return render(request, 'edit_task.html', {'task': task})