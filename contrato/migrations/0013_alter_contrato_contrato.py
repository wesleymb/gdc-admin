# Generated by Django 4.0.6 on 2022-09-09 01:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contrato', '0012_rename_contrato_id_contrato_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contrato',
            name='contrato',
            field=models.CharField(max_length=10, unique=True),
        ),
    ]