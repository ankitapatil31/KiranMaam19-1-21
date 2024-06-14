from django import forms
from froala_editor.widgets import FroalaEditor
from .models import *


class BlogForm(forms.ModelForm):
    Category = forms.ModelChoiceField(queryset=BlogCaterogy.objects.all(),
                                      widget=forms.Select(attrs={'Class': 'form-control btn btn-light dropdown-toggle"'}))

    class Meta:
        model = Blog
        fields = ['content']
