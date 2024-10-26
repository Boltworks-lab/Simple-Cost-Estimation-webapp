from django.urls import path
from .views import cost_estimate, project_list, project_add, project_details, project_edit, delete

urlpatterns = [
    path('', cost_estimate, name='home'),
    path('estimate/', project_list, name = 'project_list'),
    path('estimate/new/', project_add, name='project_add' ),
    path('detail/<int:pk>/', project_details, name='project_details'),
    path('edit/<int:pk>/', project_edit, name= 'project_edit'),
    path('delete/<int:pk>/', delete, name= 'delete')
]