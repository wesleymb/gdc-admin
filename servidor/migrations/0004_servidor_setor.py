# Generated by Django 4.0.6 on 2022-08-24 02:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('setor', '0001_initial'),
        ('servidor', '0003_alter_servidor_nome'),
    ]

    operations = [
        migrations.AddField(
            model_name='servidor',
            name='setor',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='setor.setor'),
        ),
    ]
