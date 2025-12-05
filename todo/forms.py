from django.forms import ModelForm, TextInput
from .models import Todo

class TodoForm(ModelForm):
    class Meta:
        model = Todo
        fields = ['title']
        widgets = {
            'title': TextInput(attrs={
                'placeholder': 'Enter a new todo item',
                'id': 'todo-title-input'
            })
        }