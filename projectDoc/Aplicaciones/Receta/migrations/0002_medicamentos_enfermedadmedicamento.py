# Generated by Django 5.0.3 on 2024-05-03 22:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Receta', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Medicamentos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cNombre', models.CharField(max_length=30)),
                ('bEstatus', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='EnfermedadMedicamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('IdEnfermedad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Receta.enfermedades')),
                ('IdMedicamento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Receta.medicamentos')),
            ],
        ),
    ]
