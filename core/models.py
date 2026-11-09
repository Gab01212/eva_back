from django.db import models
from django.core.validators import MinValueValidator

class EspecialidadMedica(models.Model):
    nombre = models.CharField(max_length=100, unique=True, verbose_name="Nombre de Especialidad")
    descripcion = models.TextField(verbose_name="Descripción General")
    activa = models.BooleanField(default=True, verbose_name="Vigente / Activa")

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "Especialidad Médica"
        verbose_name_plural = "Especialidades Médicas"


class PrestacionMedica(models.Model):
    ESTADOS_OPERATIVOS = [
        ('DISPONIBLE', 'Disponible'),
        ('SUSPENDIDO', 'Suspendido Temporalmente'),
        ('AGOTADO', 'Cupos Agotados'),
    ]

    codigo = models.CharField(max_length=20, unique=True, verbose_name="Código Alfanumérico")
    titulo = models.CharField(max_length=150, verbose_name="Nombre del Examen o Prestación")
    especialidad = models.ForeignKey(
        EspecialidadMedica, 
        on_delete=models.PROTECT, 
        verbose_name="Especialidad de Contexto"
    )
    descripcion = models.TextField(verbose_name="Detalle de Requisitos")
    arancel_base = models.DecimalField(
        max_digits=10, 
        decimal_places=2, 
        validators=[MinValueValidator(0)], 
        verbose_name="Arancel Base (CLP)"
    )
    duracion_minutos = models.IntegerField(
        validators=[MinValueValidator(5)], 
        verbose_name="Duración estimada (Minutos)"
    )
    estado = models.CharField(
        max_length=20, 
        choices=ESTADOS_OPERATIVOS, 
        default='DISPONIBLE', 
        verbose_name="Condición Operativa"
    )
    imagen = models.ImageField(upload_to='prestaciones/', blank=True, null=True, verbose_name="Imagen / Ilustración")
    vigente = models.BooleanField(default=True, verbose_name="Baja Lógica (Vigente)")

    def __str__(self):
        return f"[{self.codigo}] {self.titulo}"

    class Meta:
        verbose_name = "Prestación Médica"
        verbose_name_plural = "Prestaciones Médicas"