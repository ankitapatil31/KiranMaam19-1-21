from django.urls import path
from . import views



urlpatterns=[
    path('addSkill/', views.CrudView.as_view()),
    path('ajax/crud/create/', views.CreateSkillSet.as_view(), name='crud_ajax_create'),
    path('ajax/crud/update/', views.UpdateCrudSkill.as_view(), name='crud_ajax_update'),
    path('ajax/crud/delete/',  views.DeleteCrudSkill.as_view(), name='crud_ajax_delete'),

    path('addexperienceset/',views.Admin_AddExperience_details,name='AddExperience_Page'),
    path('delete<str:id>', views.delete_experience, name='delete_experience'),
    path('update34<str:id>',views.update_experience,name='update_experience'),
]