from email.charset import Charset
from email.policy import default
from random import choices
from secrets import choice
from django.db import models
from contrato.models import Contrato

# Create your models here.


class Pagamento(models.Model):
    status_choises =( 
        ('PAGO', 'PAGO'),
        ('TRAMITANDO', 'TRAMITANDO'),
        ('EM ATRASO', 'EM ATRASO'),
    )

    id = models.AutoField(primary_key=True, auto_created=True)
    id_contrato = models.ForeignKey(Contrato, models.CASCADE, blank=False, null=False)
    valor = models.FloatField(blank=False, null=False)
    data_de_vencimento = models.DateField(blank=False, null=False)
    numero_do_processo = models.CharField(max_length=30, blank=False, null=False)
    status = models.CharField(max_length=30, choices=status_choises, blank=False, null=False)

    def __str__(self) -> str:
        return str(self.id_contrato)