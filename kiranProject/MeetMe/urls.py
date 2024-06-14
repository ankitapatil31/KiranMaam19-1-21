
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.Userprofile,name='Profile_page'),
    path('PersonalInfomation/',views.personalInformation,name='PerosnalInformation_Page')

]
