from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
from .models import PrestacionMedica

def agregar_a_canasta(request, pk):
    prestacion = get_object_or_404(PrestacionMedica, pk=pk)
    canasta = request.session.get('canasta', {})

    pk_str = str(pk)
    if pk_str in canasta:
        canasta[pk_str]['cantidad'] += 1
    else:
        canasta[pk_str] = {
            'titulo': prestacion.titulo,
            'codigo': prestacion.codigo,
            'arancel': float(prestacion.arancel_base),
            'cantidad': 1
        }
    
    request.session['canasta'] = canasta
    messages.success(request, f"'{prestacion.titulo}' añadida al pre-agendamiento.")
    return redirect('catalogo')

def ver_canasta(request):
    canasta = request.session.get('canasta', {})
    subtotal = sum(item['arancel'] * item['cantidad'] for item in canasta.values())
    
    # Simulación de descuento por previsión de salud (ej: 20%)
    descuento = subtotal * 0.20
    total_final = subtotal - descuento

    return render(request, 'core/canasta.html', {
        'canasta': canasta,
        'subtotal': subtotal,
        'descuento': descuento,
        'total_final': total_final
    })

def eliminar_item_canasta(request, pk):
    canasta = request.session.get('canasta', {})
    pk_str = str(pk)
    if pk_str in canasta:
        del canasta[pk_str]
        request.session['canasta'] = canasta
        messages.info(request, "Elemento retirado de la canasta.")
    return redirect('ver_canasta')

def vaciar_canasta(request):
    if 'canasta' in request.session:
        del request.session['canasta']
        messages.info(request, "Canasta de pre-agendamiento vaciada.")
    return redirect('catalogo')

def simular_pago(request):
    if 'canasta' in request.session:
        del request.session['canasta']
    messages.success(request, "¡Pre-agendamiento generado con éxito! Se ha enviado el comprobante a su correo.")
    return redirect('catalogo')