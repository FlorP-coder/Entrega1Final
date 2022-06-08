from django.db import models

# Create your models here.
class Usuarios(models.Model):
    nombre = models.CharField (max_length=40)
    apellido = models.CharField (max_length=40)
    nacimiento = models.DateField ()
    num_cuenta = models.IntegerField()
    fecha_alta = models.DateField ()

class Productos(models.Model):
    tipo_prod = models.CharField (max_length=40)
    num_comercio = models.IntegerField()

class Costos(models.Model):
    tipo_costo = models.CharField (max_length=40)
    num_comercio = models.IntegerField()

class Autorizaciones(models.Model):
    num_cuenta = models.IntegerField()
    fecha_aut = models.DateField()
    tipo_prod = models.CharField (max_length=40)
    estado_trx = models.CharField(max_length=40)

class Presentaciones(models.Model):
    num_cuenta = models.IntegerField()
    fecha_pres = models.DateField()
    tipo_prod = models.CharField (max_length=40)