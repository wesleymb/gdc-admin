# Generated by Django 4.0.6 on 2022-08-23 01:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servidor', '0002_alter_servidor_nome'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servidor',
            name='nome',
            field=models.CharField(max_length=30),
        ),
    ]
