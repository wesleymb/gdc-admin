import datetime

from django.db import models
from django.utils import timezone
from contrato.models import Contrato
from servidor.models import Servidor
# Create your models here.

class Equipamento(models.Model):
    id = models.AutoField(primary_key=True, auto_created=True)
    codigo_identificador = models.CharField(max_length=30, blank=False, null=False)
    nome = models.CharField(max_length=30, blank=False, null=False)
    descricao = models.CharField(max_length=30, blank=False, null=False)
    contrato = models.ForeignKey(Contrato, models.CASCADE, blank=True, null=True)

    def __str__(self) -> str:
        return f'{self.nome} / {self.codigo_identificador}'

class Emprestimo(models.Model):
    id = models.AutoField(primary_key=True, auto_created=True)
    id_equipamento = models.OneToOneField(Equipamento, models.CASCADE, blank=False, null=True, unique=True)
    data_de_emprestimo = models.DateField(blank=False, null=False, default=timezone.now)
    data_de_devolucao = models.DateField(blank=True, null=True)
    servidor_responsavel = models.ForeignKey(Servidor, models.DO_NOTHING, blank=True, null=True)

    def __str__(self) -> str:
        return f'{self.id_equipamento}'