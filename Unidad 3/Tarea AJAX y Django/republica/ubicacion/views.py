from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods

# Create your views here.
ESTADOS = { #Diccionario
    'Aguascalientes': ['Aguascalientes', 'Asientos', 'Calvillo', 'Jesús María', 'Pabellón de Arteaga'],
    'Baja California': ['Ensenada', 'Mexicali', 'Playas de Rosarito', 'Tecate', 'Tijuana'],
    'Baja California Sur': ['Comondú', 'La Paz', 'Loreto', 'Los Cabos', 'Mulegé'],
    'Campeche': ['Calakmul', 'Campeche', 'Carmen', 'Champotón', 'Escárcega'],
    'Coahuila': ['Acuña', 'Monclova', 'Piedras Negras', 'Saltillo', 'Torreón'],
    'Colima': ['Colima', 'Manzanillo', 'Tecomán'],
    'Chiapas': ['Comitán', 'Palenque', 'San Cristóbal de las Casas', 'Tapachula', 'Tuxtla Gutiérrez'],
    'Chihuahua': ['Chihuahua', 'Ciudad Juárez', 'Cuauhtémoc', 'Delicias', 'Parral'],
    'Ciudad de México': ['Álvaro Obregón', 'Benito Juárez', 'Coyoacán', 'Iztapalapa', 'Tlalpan'],
    'Durango': ['Durango', 'Gómez Palacio', 'Lerdo'],
    'Guanajuato': ['Celaya', 'Guanajuato', 'Irapuato', 'León', 'Moroleón', 'Salamanca', 'Uriangato', 'Yuriria'],
    'Guerrero': ['Acapulco', 'Chilpancingo', 'Iguala', 'Zihuatanejo'],
    'Hidalgo': ['Actopan', 'Pachuca', 'Tula', 'Tulancingo'],
    'Jalisco': ['Guadalajara', 'Puerto Vallarta', 'Tlaquepaque', 'Tonalá', 'Zapopan'],
    'México': ['Ecatepec', 'Nezahualcóyotl', 'Naucalpan', 'Tlalnepantla', 'Toluca'],
    'Michoacán': ['Lázaro Cárdenas', 'Morelia', 'Uruapan', 'Zamora'],
    'Morelos': ['Cuautla', 'Cuernavaca', 'Jiutepec'],
    'Nayarit': ['Compostela', 'Tepic', 'Tuxpan'],
    'Nuevo León': ['Apodaca', 'Guadalupe', 'Monterrey', 'San Nicolás de los Garza', 'Santa Catarina'],
    'Oaxaca': ['Huajuapan de León', 'Juchitán de Zaragoza', 'Oaxaca de Juárez', 'Salina Cruz'],
    'Puebla': ['Atlixco', 'Puebla', 'San Martín Texmelucan', 'Tehuacán'],
    'Querétaro': ['Corregidora', 'Querétaro', 'San Juan del Río'],
    'Quintana Roo': ['Cancún', 'Chetumal', 'Playa del Carmen', 'Tulum'],
    'San Luis Potosí': ['Ciudad Valles', 'Matehuala', 'San Luis Potosí'],
    'Sinaloa': ['Culiacán', 'Los Mochis', 'Mazatlán'],
    'Sonora': ['Ciudad Obregón', 'Guaymas', 'Hermosillo', 'Nogales'],
    'Tabasco': ['Cárdenas', 'Comalcalco', 'Villahermosa'],
    'Tamaulipas': ['Ciudad Victoria', 'Matamoros', 'Nuevo Laredo', 'Reynosa'],
    'Tlaxcala': ['Apizaco', 'Huamantla', 'Tlaxcala'],
    'Veracruz': ['Coatzacoalcos', 'Poza Rica', 'Veracruz', 'Xalapa'],
    'Yucatán': ['Mérida', 'Tizimín', 'Valladolid'],
    'Zacatecas': ['Fresnillo', 'Guadalupe', 'Zacatecas'],
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