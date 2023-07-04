from rest_framework import serializers
from .models import TblParentesco, TblTipoMantenimiento, TblVehiculoMantenimiento

class ParentescoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TblParentesco
        fields = '__all__'

class TblVehiculoMantenimientoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TblVehiculoMantenimiento
        fields = '__all__'

class TblTipoMantenimientoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TblTipoMantenimiento
        fields = '__all__'
