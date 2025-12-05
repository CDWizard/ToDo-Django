from django.shortcuts import render
from .models import Todo

def create(request):
    if request.POST:
        title=request.POST.get('task')
        todo=Todo(title=title)
        todo.save()
    return render(request, 'create.html')

def list(request):
    todos=Todo.objects.all()
    print(todos)
    return render(request, 'list.html', {'todos': todos})

def edit(request):
    return render(request, 'edit.html')