from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from .models import TblVehiculoMantenimiento
from .models import TblParentesco, TblVehiculoMantenimiento, TblTipoMantenimiento
from .serializers import ParentescoSerializer, TblVehiculoMantenimientoSerializer, TblTipoMantenimientoSerializer
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

class ParentescoViewSet(ModelViewSet):
    queryset = TblParentesco.objects.all()
    serializer_class = ParentescoSerializer

class VehiculoMantenimientoViewSet(ModelViewSet):
    queryset = TblVehiculoMantenimiento.objects.all()
    serializer_class = TblVehiculoMantenimientoSerializer

    @method_decorator(csrf_exempt)
    @action(detail=False, methods=['post'])
    def registro_mantenimiento(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'message': 'Datos de mantenimiento guardados correctamente'})
    
    @method_decorator(csrf_exempt)
    @action(detail=True, methods=['delete'])
    def eliminar_mantenimiento(self, request, pk=None):
        mantenimiento = self.get_object()
        mantenimiento.delete()
        return Response({'message': 'Mantenimiento eliminado correctamente'})

    @method_decorator(csrf_exempt)
    @action(detail=True, methods=['put', 'patch'])
    def modificar_mantenimiento(self, request, pk=None):
        mantenimiento = self.get_object()
        serializer = self.get_serializer(mantenimiento, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'message': 'Mantenimiento modificado correctamente'})

class TblTipoMantenimientoViewSet(ModelViewSet):
    queryset = TblTipoMantenimiento.objects.all()
    serializer_class = TblTipoMantenimientoSerializer