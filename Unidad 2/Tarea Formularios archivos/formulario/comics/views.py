from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView
from django.urls import reverse_lazy
from .models import Comic
from .forms import ComicForm

# Create your views here.
class ListaComicsView(ListView):
    model = Comic
    template_name = 'comics/inicio.html'
    context_object_name = 'comics'

class SubirComicView(CreateView):
    model = Comic
    form_class = ComicForm
    template_name = 'comics/subir.html'
    success_url = reverse_lazy('lista_comics')

class EditarComicView(UpdateView):
    model = Comic
    form_class = ComicForm
    template_name = 'comics/editar.html'
    success_url = reverse_lazy('lista_comics')
    
    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields.pop('archivo') #Así ya no hay que subir por fuerza la imagen o pdf
        return form