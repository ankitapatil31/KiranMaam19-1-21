from django.contrib import messages
from django.shortcuts import render
from .models import Message,Bookappointment
# Create your views here.


def Getintouch(request):
    if request.method == "POST":
        Nm = request.POST.get('Name')
        Email = request.POST.get('EmailId')
        msg = request.POST.get('Message')
        Message.objects.create(Name=Nm, EmailId = Email, Message = msg)
        messages.success(request, "Message Send successful.")
    return render(request,'GetInTouch/Getintouch.html')


def BookAppointmentform(request):
    if request.method == 'POST':
        Nm = request.POST.get('Name')
        Email = request.POST.get('Email')
        no = request.POST.get('ContactNo')
        D = request.POST.get('MeetingTime')
        print(D)
        msg = request.POST.get('Message')
        Bookappointment.objects.create(Name=Nm, email=Email, content=msg, contactNo=no, Date=D)
        #messages.success(request, "Book Appointment Notice Send successful.")
    return render(request, 'GetInTouch/BookAppointment.html')

