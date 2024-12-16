from django.contrib import admin
from .models import Reserva

class ReservaAdmin(admin.ModelAdmin):
    list_display = ['usuario', 'fecha', 'fecha_fin', 'reserva_equipo_nombre']
    def save_model(self, request, obj, form, change):
        if not obj.usuario:
            obj.usuario = request.user  # Asigna automáticamente el usuario logueado
        super().save_model(request, obj, form, change)

    def reserva_equipo_nombre(self, obj):
        return obj.reserva_equipo.nombre  # Mostrar el nombre del equipo

    reserva_equipo_nombre.short_description = 'Equipo'

admin.site.register(Reserva, ReservaAdmin)
