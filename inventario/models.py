from django.db import models

# Create your models here.
class producto(models.Model):
    referencia=models.CharField(max_length=7)
    categoria=models.CharField(max_length=20)
    descripcion=models.CharField(max_length=200)
    precio=models.IntegerField()
    cantidad=models.IntegerField(null=True, unique=True)

class imagene(models.Model):
    referenciaFk=models.CharField(max_length=7)
    imagen=models.CharField(max_length=200)



