from rest_framework.viewsets import ModelViewSet
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from .models import TblVehiculoMantenimiento
from .models import TblParentesco, TblVehiculoMantenimiento, TblTipoMantenimiento
from .serializers import ParentescoSerializer, TblVehiculoMantenimientoSerializer, TblTipoMantenimientoSerializer

class ParentescoViewSet(ModelViewSet):
    queryset = TblParentesco.objects.all()
    serializer_class = ParentescoSerializer

class VehiculoMantenimientoViewSet(ModelViewSet):
    queryset = TblVehiculoMantenimiento.objects.all()
    serializer_class = TblVehiculoMantenimientoSerializer

    @action(detail=False, methods=['post'])
    def registro_mantenimiento(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'message': 'Datos de mantenimiento guardados correctamente'})

class TblTipoMantenimientoViewSet(ModelViewSet):
    queryset = TblTipoMantenimiento.objects.all()
    serializer_class = TblTipoMantenimientoSerializer
