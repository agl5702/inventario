# Generated by Django 5.1.4 on 2024-12-16 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0003_alter_equipo_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipo',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='inventario/images', verbose_name='Imagen'),
        ),
    ]
