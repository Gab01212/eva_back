from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from core.models import EspecialidadMedica, PrestacionMedica

class Command(BaseCommand):
    help = 'Pobla la base de datos con clasificadores iniciales, prestaciones y usuarios de prueba.'

    def handle(self, *args, **kwargs):
        self.stdout.write("Iniciando población de datos...")

        # Limpiar datos previos si es necesario (opcional)
        PrestacionMedica.objects.all().delete()
        EspecialidadMedica.objects.all().delete()

        # 1. Crear Especialidades (Clasificadores - al menos 4)
        esp1 = EspecialidadMedica.objects.create(nombre="Cardiología", descripcion="Estudio y prevención del sistema cardiovascular.", activa=True)
        esp2 = EspecialidadMedica.objects.create(nombre="Imagenología", descripcion="Exámenes de diagnóstico por imágenes.", activa=True)
        esp3 = EspecialidadMedica.objects.create(nombre="Laboratorio Clínico", descripcion="Análisis de muestras biológicas.", activa=True)
        esp4 = EspecialidadMedica.objects.create(nombre="Oftalmología", descripcion="Cuidado de la salud visual y ocular.", activa=True)

        # 2. Crear Prestaciones Principales (Al menos 8)
        PrestacionMedica.objects.create(
            codigo="CARD-01", titulo="Electrocardiograma de Reposo", especialidad=esp1,
            descripcion="Registro de la actividad eléctrica del corazón.", arancel_base=35000,
            duracion_minutos=20, estado="DISPONIBLE", vigente=True
        )
        PrestacionMedica.objects.create(
            codigo="CARD-02", titulo="Holter de Presión Arterial (MAPA)", especialidad=esp1,
            descripcion="Monitoreo continuo de presión por 24 horas.", arancel_base=65000,
            duracion_minutos=30, estado="DISPONIBLE", vigente=True
        )
        PrestacionMedica.objects.create(
            codigo="IMAG-01", titulo="Radiografía de Tórax AP/Lateral", especialidad=esp2,
            descripcion="Placa radiográfica digital de estructuras torácicas.", arancel_base=28000,
            duracion_minutos=15, estado="DISPONIBLE", vigente=True
        )
        PrestacionMedica.objects.create(
            codigo="IMAG-02", titulo="Ecotomografía Abdominal", especialidad=esp2,
            descripcion="Ultrasonido de órganos abdominales.", arancel_base=50000,
            duracion_minutos=30, estado="DISPONIBLE", vigente=True
        )
        PrestacionMedica.objects.create(
            codigo="LAB-01", titulo="Perfil Bioquímico Completo", especialidad=esp3,
            descripcion="Análisis de glucosa, colesterol, triglicéridos, etc.", arancel_base=22000,
            duracion_minutos=10, estado="DISPONIBLE", vigente=True
        )
        PrestacionMedica.objects.create(
            codigo="LAB-02", titulo="Hemograma Completo", especialidad=esp3,
            descripcion="Recuento de glóbulos rojos, blancos y plaquetas.", arancel_base=18000,
            duracion_minutos=10, estado="DISPONIBLE", vigente=True
        )
        PrestacionMedica.objects.create(
            codigo="OFT-01", titulo="Test de Agudeza Visual", especialidad=esp4,
            descripcion="Evaluación optométrica de la visión.", arancel_base=20000,
            duracion_minutos=20, estado="DISPONIBLE", vigente=True
        )
        PrestacionMedica.objects.create(
            codigo="OFT-02", titulo="Fondoscopía", especialidad=esp4,
            descripcion="Inspección del fondo del ojo y retina.", arancel_base=30000,
            duracion_minutos=15, estado="DISPONIBLE", vigente=True
        )

        # 3. Crear Usuarios de Prueba (admin y estándar)
        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser('admin', 'admin@redsalud.cl', 'admin123')
        if not User.objects.filter(username='paciente').exists():
            User.objects.create_user('paciente', 'paciente@gmail.com', 'paciente123')

        self.stdout.write(self.style.SUCCESS("¡Base de datos poblada exitosamente!"))