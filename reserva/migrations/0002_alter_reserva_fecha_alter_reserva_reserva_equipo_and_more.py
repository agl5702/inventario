# Generated by Django 5.1.4 on 2024-12-16 14:23

import django.contrib.auth.models
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0004_alter_equipo_imagen'),
        ('reserva', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='reserva',
            name='fecha',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='reserva',
            name='reserva_equipo',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='inventario.equipo'),
        ),
        migrations.AlterField(
            model_name='reserva',
            name='usuario',
            field=models.ForeignKey(default=django.contrib.auth.models.User, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
