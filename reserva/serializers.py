from rest_framework import serializers
from inventario.models import Equipo
from .models import Reserva


class ReservaSerializer(serializers.ModelSerializer):

    reserva_equipo = serializers.PrimaryKeyRelatedField(queryset=Equipo.objects.all(), required=False, allow_null=True)
    usuario = serializers.CharField(source='usuario.username', read_only=True)

    class Meta:
        model = Reserva
        fields = ['id', 'reserva_equipo', 'fecha', 'fecha_fin', 'usuario']  # Especificando los campos manualmente

    def validate(self, data):
        if data['fecha'] >= data['fecha_fin']:
            raise serializers.ValidationError("La fecha de inicio debe ser anterior a la fecha de finalización.")

        reservas_existentes = Reserva.objects.filter(
            reserva_equipo=data['reserva_equipo'],
            fecha__lt=data['fecha_fin'],
            fecha_fin__gt=data['fecha']
        )
        if reservas_existentes.exists():
            raise serializers.ValidationError("El equipo ya está reservado en este horario.")

        return data

    def create(self, validated_data):
        user = self.context['request'].user
        validated_data['usuario'] = user  # Asignar el usuario logueado

        return super().create(validated_data)
