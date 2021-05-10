from django import forms
from django.forms.widgets import TextInput

from recipes.models import Tag


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = (
            'title',
            'display_name',
            'color',
        )
        widgets = {
            'color': TextInput(attrs={'type': 'color'}),
        }
