from django.db import models
from django.contrib.auth.models import User 

# Create your models here.
class tasks(models.Model):
    title= models.CharField(max_length=100)
    description=models.CharField(max_length=100, blank=True)
    created= models.DateTimeField(auto_now_add=True)
    datecompleted=models.DateTimeField(null=True)
    important=models.BooleanField(default= False)
    User=models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) :
        return self. title + '- by' + self.User.username
    
class categoria(models.model):
    nombre=models.CharField(max_length=100)

class inventario(models.model):
    codigo=models.IntegerField()
    nombre=models.CharField(max_length=100)
    en_prestamo=models.BooleanField(default=False)
    categoria=models.ForeignKey(categoria, on_delete=models.SET_NULL)

class transaccion(models.Model):
    id_inventario=models.ForeignKey(inventario,on_delete=models.CASCADE)





