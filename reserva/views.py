from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Reserva
from .serializers import ReservaSerializer

class ReservaViewSet(viewsets.ModelViewSet):
    queryset = Reserva.objects.all()
    serializer_class = ReservaSerializer
    permission_classes = [IsAuthenticated]



    def get_queryset(self):
        """
        Filtra las reservas para que solo el usuario autenticado pueda ver sus propias reservas.
        """
        user = self.request.user
        return Reserva.objects.filter(usuario=user)  # 


    def perform_create(self, serializer):
        # Asignar automáticamente el usuario que realiza la reserva
        serializer.save(usuario=self.request.user)
