from django.db import models

# Create your models here.
class Equipo(models.Model):

    cantidad = models.IntegerField('Cantidad')
    porcentaje_avance = models.FloatField('Procentaje de avance en Hermes')
    nombre = models.CharField('Nombre del equipo',max_length=150)
    placa=models.IntegerField()
    marca = models.CharField('Marca',max_length=50)
    modelo= models.CharField('Modelo',max_length=45)
    numero_serie = models.CharField('Numero serie',max_length=45)
    imagen = models.ImageField('Imagen',upload_to='inventario/images',)
    descripcion = models.TextField('Descripcion')
    procedencia = models.CharField('Procedencia',max_length=45)
    uso=models.TextField('Uso del equipo')
    responsable = models.CharField('Responsable',max_length=75)
    numero_odc=models.IntegerField('Numero ODC')
    ano_compra=models.IntegerField('Año de compra')
    proveedor = models.CharField('Proveedor',max_length=45)
    fecha_fabricacion =models.DateField('Fecha de fabricacion')
    vida_util_ano = models.IntegerField('Vida util en años')
    fecha_instalacion = models.DateField()
    fin_deprecacion= models.DateField()
    garantia_mes = models.IntegerField()
    ubicacion = models.CharField(max_length=45)
    informacion_faltante = models.TextField()
    observaciones = models.TextField()
    estado = models.BooleanField(default=False)

    def __str__(self):
        return self.nombre

class Insumo(models.Model):
    
    codigo = models.CharField(max_length=50)
    descripcion= models.TextField()
    cantidad = models.IntegerField()
    imagen = models.ImageField()
    responsable = models.CharField(max_length=75)
    numero_odc = models.IntegerField()
    ano_compra = models.IntegerField()
    proveedor = models.CharField(max_length=75)
    ubicacion = models.CharField(max_length=50)

    def __str__(self):
        return self.descripcion