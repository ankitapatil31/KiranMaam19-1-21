from django import forms
from django.forms import ModelForm
from .models import Experiences


class SkillSetForm(forms.Form):
    Skill = forms.CharField(label='Skills',
                            max_length=100,
                            widget=forms.TextInput(
                                attrs={'class':'form-control','placeholder':'Enter Skill'}))
    Rateing = forms.IntegerField(label='Rateing on Skill',
                                 required=True,
                                 max_value=100,
                                 min_value=30,
                                 widget=forms.TextInput(
                                     attrs={'class':'form-control','placeholder':'Enter Rateing on Skill'}))


class AddExperiencesForm(forms.ModelForm):
    toDate = forms.CharField(required=False,
                             label="To",
                             widget=forms.DateInput(
                                attrs={'class': 'form-control', 'id': 'todate', 'type': 'date'}))
    currently_working = forms.NullBooleanField(
                                               required=False,
                                               label="Currently Working ",
                                               widget=forms.CheckboxInput(
                                                   attrs={'class': 'form-check-input', 'id': 'curtly_working','onclick': 'EnableDisableTextBox(this)'}))
    class Meta:
        model = Experiences
        fields = ['organization_name', 'designation', 'formDate', 'currently_working', 'toDate', 'description']
        fields_required = ['organization_name', 'designation', 'formDate', 'currently_working', 'description']
        labels = {
            "organization_name": "Organization Name",
            'currently_working': 'Currently Working',
            'designation': 'Designation',
            'formDate': 'Form',
            'toDate': 'To',
            'description': 'Description'
        }
        widgets = {
            'organization_name': forms.TextInput(
                attrs={'class': 'form-control', 'id': 'org_name', 'placeholder': 'Orgnization Name '}),
            'designation': forms.TextInput(
                attrs={'class': 'form-control', 'id': 'designation', 'placeholder': 'Designation'}),
            'currently_working': forms.CheckboxInput(
                attrs={'class': 'form-check-input', 'id': 'curtly_working', 'value': 'false',
                       'onclick': 'EnableDisableTextBox(this)'}),
            'formDate': forms.DateInput(
                attrs={'class': 'form-control', 'id': 'formdate', 'type': 'date'}),
            'toDate': forms.DateInput(
                attrs={'class': 'form-control', 'id': 'todate', 'type': 'month'}),
            'description': forms.Textarea(
                attrs={'class': 'form-control', 'id': 'description', 'placeholder': 'Designation'}),
        }

