from django.forms import ModelForm, TextInput, FileInput
from .models import Todo

class TodoForm(ModelForm):
    class Meta:
        model = Todo
        fields = ['title', 'image']
        widgets = {
            'title': TextInput(attrs={
                'placeholder': 'Enter a new todo item',
                'id': 'todo-title-input'
            }),
            'image': FileInput(attrs={
                'id': 'todo-image-input'
            })
        }