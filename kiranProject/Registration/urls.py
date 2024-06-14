from django.urls import path
from . import views

urlpatterns = [
    path('Registration/', views.RegistrationView, name='Registration_Form'),
    path('', views.LoginView, name='Login_Form'),
    path('Logout/',views.LogoutView, name='LogoutPage')
]
