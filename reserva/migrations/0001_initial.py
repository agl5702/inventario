# Generated by Django 5.1.4 on 2024-12-14 15:52

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('inventario', '0003_alter_equipo_imagen'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Reserva',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('fecha_fin', models.DateTimeField()),
                ('reserva_equipo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventario.equipo')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'constraints': [models.UniqueConstraint(fields=('reserva_equipo', 'fecha', 'fecha_fin', 'usuario'), name='unique_reservation_per_equipo')],
            },
        ),
    ]
