from django.db import models

# Create your models here.
class Tabulador(models.Model):
    fecha_final = models.DateField(blank=True, null=True)
    fecha_inicial = models.DateField(blank=True, null=True)
    zona_economica = models.IntegerField(blank=True, null=True, default=2)
    nivel = models.CharField(max_length=4, blank=True, null=True)
    rango = models.IntegerField(blank=True, null=True, default=0)
    sueldo = models.DecimalField(max_digits=9, decimal_places=2, blank=True, null=True, default=0)
    compensacion = models.DecimalField(max_digits=9, decimal_places=2, blank=True, null=True, default=0)

class Ispt(models.Model):
    fecha_final = models.DateField(blank=True, null=True)
    fecha_inicial = models.DateField(blank=True, null=True)
    tipo_tabla = models.CharField(max_length=4, blank=True, null=True)
    limite_inferior = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True, default=0)
    limite_superior = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True, default=0)
    cuota_fija = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True, default=0)
    excedente = models.DecimalField(max_digits=9, decimal_places=2, blank=True, null=True, default=0)
    bruto = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True, default=0)
