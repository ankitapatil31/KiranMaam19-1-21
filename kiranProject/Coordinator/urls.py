from django.urls import path
from . import views

urlpatterns = [
    path('',views.getCoordinatorInformation,name='MitraCoordinatorInformation_page')
    ]