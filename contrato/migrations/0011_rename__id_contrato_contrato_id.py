# Generated by Django 4.0.6 on 2022-08-25 00:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contrato', '0010_alter_contrato_observacao'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contrato',
            old_name='_id',
            new_name='contrato_id',
        ),
    ]