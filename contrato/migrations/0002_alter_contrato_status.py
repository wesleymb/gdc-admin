# Generated by Django 4.0.6 on 2022-08-21 04:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contrato', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contrato',
            name='status',
            field=models.TextField(choices=[('ATIVO', 'ATIVO'), ('TRAMITANDO', 'TRAMITANDO'), ('INATIVO', 'INATIVO')]),
        ),
    ]