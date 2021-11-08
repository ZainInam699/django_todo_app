from django import forms
from .models import *
class ToDoForm(forms.ModelForm):
    class Meta:
        model  = ToDo
        fields = ('item',)

        widgets = {
            'item': forms.TextInput(attrs={'Placeholder': 'Add Items', 'autofocus':True}),
        }
