from django.contrib import admin
from inventario.models import Equipo, Insumo


# Register your models here.
class EquipoAdmin(admin.ModelAdmin):
    list_display = ('cantidad', 'nombre', 'descripcion')
    search_fields = ('nombre', 'descripcion')
    list_filter = ('descripcion', 'nombre')
    ordering = ('nombre',)
    
admin.site.register(Equipo, EquipoAdmin)
admin.site.register(Insumo)
