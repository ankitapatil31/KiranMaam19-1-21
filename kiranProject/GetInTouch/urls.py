
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.Getintouch ,name='GetInTouch_page'),
    path('BookAppointment',views.BookAppointmentform ,name='BookAppointment_Page'),


]
