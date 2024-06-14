from django.http import HttpResponseRedirect
from django.shortcuts import render
from .form import RegistrationFm, LoginForm
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout  # add this
from django.contrib import messages


# Create your views here.

def RegistrationView(request):
    if request.method == 'POST':
        registrationform = RegistrationFm(request.POST)
        if registrationform.is_valid():
            registrationform.save()
            messages.success(request, "Registration successful.")
    else:
        registrationform = RegistrationFm()
    return render(request, 'Registration/registrationform.html', {'RegistrationForm': registrationform})


def LoginView(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            form = LoginForm(request=request, data=request.POST)
            if form.is_valid():
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']
                user = authenticate(username=username, password=password)

                if user is not None:
                    login(request, user)
                    messages.info(request, f"You are now logged in as {username}.")
                    return HttpResponseRedirect('/')
                else:
                    messages.error(request, "Invalid username or password.")
            else:
                messages.error(request, "Invalid username or password.")
        else:
            form = LoginForm()
        return render(request=request, template_name="Registration/Login.html", context={"Loginform": form})
    else:
        return HttpResponseRedirect('/')


def LogoutView(request):
    logout(request)
    return HttpResponseRedirect('/')
