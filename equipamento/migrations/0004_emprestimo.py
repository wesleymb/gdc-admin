# Generated by Django 4.1.1 on 2022-09-15 01:54

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('servidor', '0006_alter_servidor_setor'),
        ('equipamento', '0003_delete_emprestimo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Emprestimo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('data_de_emprestimo', models.DateField(default=datetime.date(2022, 9, 14))),
                ('data_de_devolucao', models.DateField(blank=True, null=True)),
                ('id_equipamento', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='equipamento.equipamento')),
                ('servidor_responsavel', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='servidor.servidor')),
            ],
        ),
    ]
