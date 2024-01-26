# Archivo creado para mejor ordenamiento de las urls
from django.urls import path
from myapp import views

urlpatterns = [
    path('', views.hello),
    path('about/', views.about),
]