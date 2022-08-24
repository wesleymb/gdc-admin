# Generated by Django 4.0.6 on 2022-08-23 01:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contrato', '0006_contrato_contato_da_empresa'),
    ]

    operations = [
        migrations.AddField(
            model_name='contrato',
            name='email_da_empresa',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='contrato',
            name='telefone',
            field=models.CharField(default='', max_length=15),
        ),
        migrations.AlterField(
            model_name='contrato',
            name='contato_da_empresa',
            field=models.CharField(default='', max_length=100),
        ),
    ]