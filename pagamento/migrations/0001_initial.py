# Generated by Django 4.0.6 on 2022-08-26 01:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contrato', '0012_rename_contrato_id_contrato_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pagamento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('status', models.CharField(choices=[('PAGO', 'PAGO'), ('TRAMITANDO', 'TRAMITANDO'), ('EM ATRASO', 'EM ATRASO')], max_length=30)),
                ('data_de_vencimento', models.DateField()),
                ('valor', models.FloatField()),
                ('numero_do_processo', models.CharField(max_length=30)),
                ('id_contrato', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contrato.contrato')),
            ],
        ),
    ]
