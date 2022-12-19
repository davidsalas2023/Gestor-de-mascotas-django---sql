from django.db import models

class Mascotas(models.Model):
    idmascota= models.IntegerField(max_length=60)
    nombre= models.CharField(max_length=60)
    especie= models.CharField(max_length=60)
    class Meta:
        db_table='mascotas'
