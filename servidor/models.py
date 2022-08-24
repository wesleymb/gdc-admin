from django.db import models
from setor.models import Setor

# Create your models here.

class Servidor(models.Model):
    _id = models.AutoField(primary_key=True, auto_created=True)
    nome = models.CharField(max_length=50)
    id_funcional = models.CharField(max_length=10)
    setor = models.ForeignKey(Setor, models.SET_DEFAULT, blank=False, null=False ,default=1)

    def __str__(self) -> str:
        return self.nome