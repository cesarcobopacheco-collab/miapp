from django.db import models

class Registro(models.Model):
    numero = models.IntegerField(default=0)
    codigo = models.CharField(max_length=50, blank=True, default='')
    chip = models.CharField(max_length=50, blank=True, default='')
    sexo = models.CharField(max_length=10, blank=True, default='')
    raza = models.CharField(max_length=50, blank=True, default='')
    color = models.CharField(max_length=50, blank=True, default='')
    detalle = models.TextField(blank=True, null=True)
    lote = models.CharField(max_length=100, blank=True, default='')
    sector = models.CharField(max_length=100, blank=True, default='')
    fecha = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.codigo

# Create your models here.
