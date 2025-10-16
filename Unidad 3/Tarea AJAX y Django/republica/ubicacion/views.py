from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
def inicio(request):
    return render(request, 'ubicacion/inicio.html')