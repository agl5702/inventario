from django.urls import path,include
from inventario.views import EquipoView, InsumoView
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'Equipos',EquipoView, 'Equipos')
router.register(r'Insumos',InsumoView, 'Insumos')


urlpatterns = [
    path('',include(router.urls)),
]
