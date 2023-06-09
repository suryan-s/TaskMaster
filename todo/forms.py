from django import forms
from .models import TodoItem


class TodoItemForm(forms.ModelForm):
    class Meta:
        model = TodoItem
        fields = "__all__"
        exclude = ['username', 'created_at']
