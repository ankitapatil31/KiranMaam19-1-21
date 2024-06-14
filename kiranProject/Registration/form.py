from .models import Registration
from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UsernameField
from django.contrib.auth.models import User
from django.utils.translation import gettext,gettext_lazy as _


class RegistrationFm(UserCreationForm):
    password1 = forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter Password'}))
    password2 = forms.CharField(label='Confirm Password(again)',widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'ReEnter Password'}))
    class Meta:
        model = User
        fields = ['username','first_name', 'last_name']
        labels={
            'username': 'EmailID','first_name':'First Name','last_name':'Last Name'
        }
        widgets={
            'first_name':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Your First Name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control','placeholder':'Enter Your Last Name'}),
            'username': forms.EmailInput(attrs={'class': 'form-control','placeholder':'Email'}),
        }
# EmailID = forms.EmailField(label='Email:', widget=forms.EmailInput(attrs={'class': 'form-control', 'id': ''}))
# MobileNo = forms.IntegerField(label="Mobile No:", widget=forms.TextInput(attrs={'class': 'form-control', 'patten': '[789][0-9]{9}'}))
# Password = forms.CharField(label="Paasword:", widget=forms.PasswordInput(attrs={'class': 'form-control'}))
# ConfirmPassword = forms.CharField(label="ConfirmPassword:", widget=forms.PasswordInput(attrs={'class': 'form-control'}))

class LoginForm(AuthenticationForm):
    username = UsernameField(label='EmailID',widget=forms.TextInput(attrs={'class':'form-control','autofocus':True}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','autocomplete':'Current-password'}))