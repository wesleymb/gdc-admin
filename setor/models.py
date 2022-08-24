from django.db import models

# Create your models here.


class Setor(models.Model):
    _id = models.AutoField(primary_key=True, auto_created=True)
    nome = models.CharField(max_length=30, blank=False, null=False)

    def __str__(self) -> str:
        return self.nome