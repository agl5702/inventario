from rest_framework.routers import DefaultRouter
from reserva.views import ReservaViewSet
from django.urls import path,include

router = DefaultRouter()

router.register('reservas', ReservaViewSet, basename='reserva')

urlpatterns = [
    path('',include(router.urls)),
]
