from django.shortcuts import render
from .models import Todo
from .forms import TodoForm

def create(request):
    if request.POST:
        todoForm = TodoForm(request.POST)
        if todoForm.is_valid():
            todoForm.save()
    else:
        todoForm = TodoForm()
    return render(request, 'create.html', {'form': todoForm})

def list(request):
    todos=Todo.objects.all()
    return render(request, 'list.html', {'todos': todos})

def edit(request):
    return render(request, 'edit.html')