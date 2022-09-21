from django.db import models
from servidor.models import Servidor

# Create your models here.
class Contrato(models.Model):
    status_ativo = (
        ('ATIVO', 'ATIVO'),
        ('TRAMITANDO', 'TRAMITANDO'),
        ('INATIVO', 'INATIVO'),
    )


    id = models.AutoField(primary_key=True, auto_created=True)
    contrato = models.CharField(max_length=10, blank=False, null=False, unique=True)
    numero_de_processo = models.CharField(max_length=50, db_column='numeroDeProcesso', blank=False, null=False)  # Field name made lowercase.
    objeto = models.CharField(max_length=100, blank=False, null=False)
    empresa = models.CharField(max_length=100, blank=False, null=False)
    data_assinatura = models.DateField(blank=False, null=False)  # Field name made lowercase.
    data_termino = models.DateField(blank=False, null=False)  # Field name made lowercase.
    vencimento = models.DateField(blank=False, null=False)
    servidor_gestor = models.ForeignKey(Servidor, models.DO_NOTHING, blank=False, null=False)  # Field name made lowercase.
    status = models.CharField(max_length=20, choices=status_ativo,blank=False, null=False)
    valor = models.FloatField(blank=True, null=True)
    contato_da_empresa = models.CharField(max_length=100, blank=False, null=False, default='')
    email_da_empresa = models.CharField(max_length=50, blank=False, null=False, default='')
    telefone = models.CharField(max_length=15, blank=False, null=False, default='')
    observacao = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self) -> str:
        return self.contrato