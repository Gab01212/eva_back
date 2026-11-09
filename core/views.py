from django.shortcuts import render
from .models import PrestacionMedica, EspecialidadMedica

def catalogo_prestaciones(request):
    prestaciones = PrestacionMedica.objects.filter(vigente=True).select_related('especialidad')
    especialidades = EspecialidadMedica.objects.filter(activa=True)
    return render(request, 'core/catalogo.html', {
        'prestaciones': prestaciones,
        'especialidades': especialidades
    })

def detalle_prestacion(request, pk):
    # Definición temporal si aún no la tienes completa
    return render(request, 'core/detalle.html')

def crear_prestacion(request):
    return render(request, 'core/form_prestacion.html')

def editar_prestacion(request, pk):
    return render(request, 'core/form_prestacion.html')

def eliminar_prestacion(request, pk):
    return render(request, 'core/eliminar_confirmar.html')

def agregar_a_canasta(request, pk):
    return redirect('catalogo')

def ver_canasta(request):
    return render(request, 'core/canasta.html')

def eliminar_item_canasta(request, pk):
    return redirect('ver_canasta')

def vaciar_canasta(request):
    return redirect('catalogo')

def simular_pago(request):
    return redirect('catalogo')