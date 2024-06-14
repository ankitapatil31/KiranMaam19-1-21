from django.shortcuts import render
from .models import PersonalInfo,FacultyDevelopment
from adminpanal.models import Skillset, Experiences

# Create your views here.


def Userprofile(request):
    skills = Skillset.objects.all()
    experience = Experiences.objects.all()
    FDP = FacultyDevelopment.objects.all()
    return render(request, 'MeetMe/Profile.html', {'skills': skills, 'experiences': experience,'FDP':FDP})


def personalInformation(request):
    PersonalInformation = PersonalInfo.objects.all()
    return render(request,'MeetMe/PersonalInformation.html',{'personalinfor':PersonalInformation})