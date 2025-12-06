from django.shortcuts import render
from .models import Todo
from .forms import TodoForm

def create(request):
    if request.POST:
        todoForm = TodoForm(request.POST, request.FILES)
        if todoForm.is_valid():
            todoForm.save()
    else:
        todoForm = TodoForm()
    return render(request, 'create.html', {'form': todoForm})

def list(request):
    todos=Todo.objects.all()
    return render(request, 'list.html', {'todos': todos})

def edit(request, id):
    instance = Todo.objects.get(pk=id)
    if request.POST:
        todoForm = TodoForm(request.POST, instance=instance)
        if todoForm.is_valid():
            todoForm.save()
        todos=Todo.objects.all()
        return render(request, 'list.html', {'todos': todos})
    else:
        todoForm = TodoForm(instance=instance)
    return render(request, 'create.html', {'form': todoForm})

def delete(request, id):
    instance = Todo.objects.get(pk=id)
    instance.delete()
    todos=Todo.objects.all()
    return render(request, 'list.html', {'todos': todos})