from django.db import models


class Especie(models.Model):
    idespecie = models.IntegerField(max_length=60)
    nombre = models.CharField(max_length=60)
    class Meta:
        db_table = 'especie'

# Create your models here.
