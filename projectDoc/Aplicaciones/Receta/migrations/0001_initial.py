# Generated by Django 5.0.3 on 2024-05-02 23:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Enfermedades',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cNombre', models.CharField(max_length=30)),
                ('bEstatus', models.BooleanField(default=True)),
            ],
        ),
    ]
