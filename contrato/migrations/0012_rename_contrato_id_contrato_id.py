# Generated by Django 4.0.6 on 2022-08-25 00:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contrato', '0011_rename__id_contrato_contrato_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contrato',
            old_name='contrato_id',
            new_name='id',
        ),
    ]