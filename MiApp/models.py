from django.db import models



class Servicio(models.Model):
    nombre_Servicio = models.CharField(max_length=50)
    tipo = models.CharField(max_length=50)
    precio = models.CharField(max_length=50)
    
    def __str__(self) :
        return f"{self.id} - {self.nombre_servicio}"


class Compra(models.Model):
    fecha_compra = models.CharField(max_length=50)
    proveedor = models.CharField(max_length=50)
    importe_compra = models.CharField(max_length=50)
    
    def __str__(self) :
        return f"{self.id} - {self.proveedor}"

class Proveedor(models.Model):
    nombre = models.CharField(max_length=50)
    domicilio = models.CharField(max_length=50)
    contacto = models.CharField(max_length=50)
    
    def __str__(self) :
        return f"{self.id} - {self.nombre}"
    







