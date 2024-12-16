from django.db import models

# Create your models here.
class Equipo(models.Model):

    cantidad = models.IntegerField('Cantidad', null=True)
    porcentaje_avance = models.FloatField('Porcentaje de avance en Hermes', null=True)
    nombre = models.CharField('Nombre del equipo', max_length=150, null=True)
    placa = models.CharField(null=True,max_length=50)
    marca = models.CharField('Marca', max_length=50, null=True)
    modelo = models.CharField('Modelo', max_length=45, null=True)
    numero_serie = models.CharField('Numero serie', max_length=45, null=True)
    imagen = models.ImageField('Imagen', upload_to='inventario/images', blank=True, null=True)
    descripcion = models.TextField('Descripcion', null=True)
    procedencia = models.CharField('Procedencia', max_length=45, null=True)
    uso = models.TextField('Uso del equipo', null=True)
    responsable = models.CharField('Responsable', max_length=75, null=True)
    numero_odc = models.CharField('Numero ODC', null=True,max_length=50)
    ano_compra = models.CharField('Año de compra', null=True,max_length=50)
    proveedor = models.CharField('Proveedor', max_length=45, null=True)
    fecha_fabricacion = models.CharField('Fecha de fabricacion', null=True,max_length=50)
    vida_util_ano = models.CharField('Vida util en años', null=True,max_length=50)
    fecha_instalacion = models.CharField(null=True,max_length=50)
    fin_deprecacion = models.CharField(null=True,max_length=50)
    garantia_mes = models.CharField(null=True,max_length=50)
    ubicacion = models.CharField(max_length=45, null=True)
    informacion_faltante = models.TextField(null=True)
    observaciones = models.TextField(null=True)
    estado = models.BooleanField(default=False, null=True)

    def __str__(self):
        return self.nombre if self.nombre else 'Equipo sin nombre'

class Insumo(models.Model):
    
    codigo = models.CharField(max_length=50,blank=True,null=True)
    descripcion= models.TextField()
    cantidad = models.IntegerField()
    imagen = models.ImageField(blank=True,null=True)
    responsable = models.CharField(max_length=75)
    numero_odc = models.IntegerField()
    ano_compra = models.IntegerField()
    proveedor = models.CharField(max_length=75,blank=True,null=True)
    ubicacion = models.CharField(max_length=50)

    def __str__(self):
        return self.descripcion