from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.db.models import Q
from django.core.paginator import Paginator
from django.contrib import messages
from .models import PrestacionMedica, EspecialidadMedica
from .forms import PrestacionMedicaForm

# R (Read - Catálogo Público)
def catalogo_prestaciones(request):
    query = request.GET.get('q', '')
    especialidad_id = request.GET.get('especialidad', '')
    
    prestaciones = PrestacionMedica.objects.filter(vigente=True).select_related('especialidad')

    if query:
        prestaciones = prestaciones.filter(
            Q(titulo__icontains=query) | 
            Q(codigo__icontains=query) | 
            Q(descripcion__icontains=query)
        )
    
    if especialidad_id:
        prestaciones = prestaciones.filter(especialidad_id=especialidad_id)

    paginator = Paginator(prestaciones, 4) # 4 por página para probar paginación
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    especialidades = EspecialidadMedica.objects.filter(activa=True)

    return render(request, 'core/catalogo.html', {
        'page_obj': page_obj,
        'especialidades': especialidades,
        'query': query,
        'especialidad_id': especialidad_id
    })

def detalle_prestacion(request, pk):
    prestacion = get_object_or_404(PrestacionMedica, pk=pk)
    return render(request, 'core/detalle.html', {'prestacion': prestacion})

# C (Create - Protegido por Staff)
@login_required
@user_passes_test(lambda u: u.is_staff)
def crear_prestacion(request):
    if request.method == 'POST':
        form = PrestacionMedicaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Prestación médica creada exitosamente.")
            return redirect('catalogo')
    else:
        form = PrestacionMedicaForm()
    return render(request, 'core/form_prestacion.html', {'form': form, 'accion': 'Crear'})

# U (Update - Protegido por Staff)
@login_required
@user_passes_test(lambda u: u.is_staff)
def editar_prestacion(request, pk):
    prestacion = get_object_or_404(PrestacionMedica, pk=pk)
    if request.method == 'POST':
        form = PrestacionMedicaForm(request.POST, request.FILES, instance=prestacion)
        if form.is_valid():
            form.save()
            messages.success(request, "Prestación actualizada correctamente.")
            return redirect('catalogo')
    else:
        form = PrestacionMedicaForm(instance=prestacion)
    return render(request, 'core/form_prestacion.html', {'form': form, 'accion': 'Editar'})

# D (Delete / Baja Lógica - Protegido por Staff)
@login_required
@user_passes_test(lambda u: u.is_staff)
def eliminar_prestacion(request, pk):
    prestacion = get_object_or_404(PrestacionMedica, pk=pk)
    if request.method == 'POST':
        # Baja lógica recomendada
        prestacion.vigente = False
        prestacion.save()
        messages.warning(request, f"La prestación '{prestacion.titulo}' fue dada de baja lógicamente.")
        return redirect('catalogo')
    return render(request, 'core/eliminar_confirmar.html', {'prestacion': prestacion})