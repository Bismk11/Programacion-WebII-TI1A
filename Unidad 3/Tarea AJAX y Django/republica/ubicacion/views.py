from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods

# Create your views here.
# Diccionario principal: nombre del estado como clave
ESTADOS = {
    'Jalisco': ['Guadalajara', 'Zapopan', 'Tlaquepaque'],
    'Nuevo León': ['Monterrey', 'San Nicolás', 'Apodaca'],
    'CDMX': ['Coyoacán', 'Iztapalapa', 'Benito Juárez'],
}

@require_http_methods(["GET"])
def inicio(request):
    estados = list(ESTADOS.keys())
    return render(request, 'ubicacion/inicio.html', {'estados': estados})


@require_http_methods(["GET"])
def get_municipios(request):
    is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'

    if is_ajax:
        estado = request.GET.get('estado')
        if estado in ESTADOS:
            municipios = ESTADOS[estado]
            return JsonResponse({'municipios': municipios})
        return JsonResponse({'error': 'Estado no encontrado'}, status=400)

    return JsonResponse({'error': 'Solicitud inválida'}, status=400)