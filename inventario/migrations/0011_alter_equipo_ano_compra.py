# Generated by Django 5.1.4 on 2024-12-16 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0010_alter_equipo_fecha_fabricacion_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipo',
            name='ano_compra',
            field=models.CharField(max_length=50, null=True, verbose_name='Año de compra'),
        ),
    ]
