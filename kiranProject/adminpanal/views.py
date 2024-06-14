import json
from django.http import HttpResponseRedirect, HttpResponse
from django.views.generic import ListView
from django.views.generic import View
from django.http import JsonResponse
from django.shortcuts import render
from .models import Skillset, Experiences
from .forms import SkillSetForm, AddExperiencesForm
from .models import SkillInfoSerializer


# Create your views here.

class CrudView(ListView):
    model = Skillset
    template_name = 'adminpanal/AddSkill.html'
    context_object_name = 'skillset'


class CreateSkillSet(View):
    def get(self, request):
        skill = request.GET.get('skill', None)
        rateing = request.GET.get('rateing', None)
        print(skill)
        print(rateing)
        obj = Skillset(Skill=skill, Rateing=rateing)
        obj.save()
        skill = {'skill': obj.Skill, 'rateing': obj.Rateing}
        data = {
            'skill': skill
        }
        return JsonResponse(data)


class UpdateCrudSkill(View):
    def get(self, request):
        id1 = request.GET.get('id', None)
        skill1 = request.GET.get('skill', None)
        rateing1 = request.GET.get('rateing', None)
        obj = Skillset.objects.get(id=id1)
        obj.Skill = skill1
        obj.Rateing = rateing1
        obj.save()

        skill = {'id': obj.id, 'Skill': obj.Skill, 'Rateing': obj.Rateing}

        data = {
            'skill': skill
        }
        return JsonResponse(data)


class DeleteCrudSkill(View):
    def get(self, request):
        id1 = request.GET.get('id', None)
        Skillset.objects.get(id=id1).delete()
        data = {
            'deleted': True
        }
        return JsonResponse(data)


def Admin_AddExperience_details(request):
    if request.method == 'POST':
        experience_fm = AddExperiencesForm(request.POST)
        if experience_fm.is_valid():
            currently_working = experience_fm.cleaned_data['currently_working']
            formDate = experience_fm.cleaned_data['formDate']
            toDate = experience_fm.cleaned_data['toDate']
            organization_name = experience_fm.cleaned_data['organization_name']
            designation = experience_fm.cleaned_data['designation']
            description = experience_fm.cleaned_data['description']
            print(currently_working)
            AddExperiences = Experiences(currently_working=currently_working, formDate=formDate, toDate=toDate,
                                         organization_name=organization_name, designation=designation,
                                         description=description)
            AddExperiences.save()
    else:
        experience_fm = AddExperiencesForm()
    experiences = Experiences.objects.all()
    return render(request, 'adminpanal/AddExperience.html',
                  {'Experience_form': experience_fm, 'experiences': experiences})


def delete_experience(request, id):
    if request.method == 'POST':
        Experience_ID = Experiences.objects.get(pk=id)
        Experience_ID.delete()
        return HttpResponseRedirect('/addexperienceset')


def update_experience(request, id):
    print(id, type(id))
    if request.method == 'POST':
        UID = Experiences.objects.get(pk=id)
        fm = AddExperiencesForm(request.POST, instance=UID)
        if fm.is_valid():
            fm.save()
        return HttpResponseRedirect('/addexperienceset')
    else:
        UID = Experiences.objects.get(pk=id)
        fm = AddExperiencesForm(instance=UID)
    return render(request, 'adminpanal/updateExperience.html', {'Experience_form': fm})
