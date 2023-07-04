from django.urls import include, path
from rest_framework import routers
from .views import ParentescoViewSet, VehiculoMantenimientoViewSet, TblTipoMantenimientoViewSet

router = routers.DefaultRouter()
router.register(r'parentesco', ParentescoViewSet)
router.register(r'vehiculo-mantenimiento', VehiculoMantenimientoViewSet)
router.register(r'tipos-mantenimiento', TblTipoMantenimientoViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]