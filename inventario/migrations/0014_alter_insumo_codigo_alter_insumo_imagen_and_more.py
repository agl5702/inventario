# Generated by Django 5.1.4 on 2024-12-16 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0013_alter_equipo_placa'),
    ]

    operations = [
        migrations.AlterField(
            model_name='insumo',
            name='codigo',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='insumo',
            name='imagen',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='insumo',
            name='proveedor',
            field=models.CharField(blank=True, max_length=75),
        ),
    ]
