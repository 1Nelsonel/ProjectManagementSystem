# urls.py
from django.urls import path

from . import views

urlpatterns = [
    path('projects/', views.project_list, name='project_list'),
    path('projects/<int:pk>/', views.project_detail, name='project_detail'),
    path('projects/<int:pk>/tasks/create/', views.task_create, name='task_create'),
    path('tasks/<int:pk>/update/', views.task_update, name='task_update')
]