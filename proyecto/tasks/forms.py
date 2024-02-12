from django.forms import ModelForm
from .models import*

class Transaccion(ModelForm):
    class Meta:# metadatos - manejo de modelo y las filas que tendra
        models = Usuario

        fields=['nombre']
        


