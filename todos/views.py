# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Todo


def index(request):
    todos = Todo.objects.all()[:10]
    context = {
        'todos': todos
    }
    return render(request,'todos/index.html',context)

def detail(request,pk):
    todo = Todo.objects.get(id=pk)
    context = {
        'todo': todo
    }
    return render(request,'todos/detail.html',context)

def add(request):
    if request.method == "POST":
       title = request.POST['title']
       text = request.POST['text']
       todo = Todo(title=title,text=text)
       todo.save()
       return redirect('/todos')
    else:
        return render(request, 'todos/add.html')
