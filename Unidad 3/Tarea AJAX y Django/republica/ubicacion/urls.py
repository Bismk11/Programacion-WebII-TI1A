from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('ajax/municipios/', views.get_municipios, name='get_municipios'),
]
