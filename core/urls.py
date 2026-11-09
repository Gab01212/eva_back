from django.urls import path
from . import views

urlpatterns = [
    path('', views.catalogo_prestaciones, name='catalogo'),
    path('prestacion/<int:pk>/', views.detalle_prestacion, name='detalle_prestacion'),
    path('prestacion/crear/', views.crear_prestacion, name='crear_prestacion'),
    path('prestacion/editar/<int:pk>/', views.editar_prestacion, name='editar_prestacion'),
    path('prestacion/eliminar/<int:pk>/', views.eliminar_prestacion, name='eliminar_prestacion'),
    
    # Canasta / Sesiones
    path('canasta/agregar/<int:pk>/', views.agregar_a_canasta, name='agregar_a_canasta'),
    path('canasta/', views.ver_canasta, name='ver_canasta'),
    path('canasta/eliminar/<int:pk>/', views.eliminar_item_canasta, name='eliminar_item_canasta'),
    path('canasta/vaciar/', views.vaciar_canasta, name='vaciar_canasta'),
    path('canasta/simular-pago/', views.simular_pago, name='simular_pago'),
]