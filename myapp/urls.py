# Archivo creado para mejor ordenamiento de las urls
from django.urls import path
from myapp import views

urlpatterns = [
    path('', views.index, name = "index"),
    path('about/', views.about, name = "about"),
    path('hello/<str:username>', views.hello, name="hello"),
    path('projects/', views.projects, name="projects"),
    path('projects/<int:id>', views.project_detail, name="project_detail"),
    path('tasks/', views.tasks, name="tasks"),
    path('create_tasks/', views.create_tasks, name="create_task"),
    path('create_new_projects/', views.create_projects, name="create_project"),
]