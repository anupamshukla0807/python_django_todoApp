from django import forms
from .models import TodoItem  # Import the TodoItem model


class TodoItemForm(forms.Form):
    title = forms.CharField(max_length=200)
    task=forms.CharField(max_length=400)
    completed = forms.BooleanField(required=False)