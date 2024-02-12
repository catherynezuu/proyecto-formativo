from django.db import models
from django.contrib.auth.models import User 


class Categoria(models.Model):
    nombre=models.CharField(max_length=100)

class Inventario(models.Model):
    codigo=models.IntegerField()
    nombre=models.CharField(max_length=100)
    en_prestamo=models.BooleanField(default=False)
    categoria=models.ForeignKey(Categoria, on_delete=models.CASCADE)

class Usuario(models.Model): 
    cedula=models.IntegerField()
    nombre=models.CharField(max_length=100)

class Tipo(models.Model):
    nombre=models.CharField(max_length=100)
    
class Transaccion(models.Model):
    id_inventario=models.ForeignKey(Inventario,on_delete=models.CASCADE)
    id_usuario=models.ForeignKey(Usuario,on_delete=models.CASCADE)
    id_tipo=models.ForeignKey(Tipo, on_delete=models.CASCADE)
    fecha_hora=models.DateTimeField(auto_now_add=True)





