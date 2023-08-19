from django.shortcuts import render, redirect
from . models import *
from .forms import *

# Create your views here.

def index(request):
    todos = Todo.objects.all()
    
    form = TodoForm()

    if request.method == 'POST':
        form = TodoForm(request.POST)

        if form.is_valid():
            form.save()

        return redirect('/')
    return render(request, template_name='todo/index.html', context={'todos': todos, 'form': form})


def update(request, pk):
    todo = Todo.objects.get(id=pk)

    form = TodoForm(instance=todo)

    if request.method == 'POST':
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect('/')

    return render(request, template_name='todo/update.html', context={'form': form})

def delete(request, pk):
    item = Todo.objects.get(id=pk)

    if request.method == 'POST':
        item.delete()
        return redirect('/')
    return render(request, template_name='todo/delete.html', context={'item': item})