# Generated by Django 4.0.6 on 2022-08-21 01:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Servidor',
            fields=[
                ('_id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=30)),
                ('id_funcional', models.CharField(max_length=10)),
            ],
        ),
    ]
