from django.http import HttpResponse
from django.shortcuts import render
<<<<<<< HEAD
from todo.models import Task

def home(request):
    tasks=Task.objects.filter(is_completed =False).order_by("created_at")
    contaxt={
        'tasks':tasks
    }
    return render (request,"home.html",contaxt)
=======

def home(request):
    return render (request,"home.html")
>>>>>>> 044fec3b70288c19259c59e7d181a41422eb44e0
