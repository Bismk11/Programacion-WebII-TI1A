from django.urls import path
from . import views

urlpatterns = [
    path('', views.ListaComicsView.as_view(), name='lista_comics'),
    path('subir/', views.SubirComicView.as_view(), name='subir_comic'),
    path('editar/<int:pk>/', views.EditarComicView.as_view(), name='editar_comic'),
]