# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class TblAlumno(models.Model):
    alumno_id = models.AutoField(primary_key=True)
    alumno_nombre = models.CharField(max_length=255)
    alumno_apellido = models.CharField(max_length=255)
    alumno_fecha_nacimiento = models.DateField(blank=True, null=True)
    alumno_foto = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = 'tbl_alumno'


class TblAlumnoHorario(models.Model):
    alumno_horario_id = models.AutoField(primary_key=True)
    alumno_horario_dia = models.CharField(max_length=45)
    alumno_horario_ingreso = models.TimeField()
    alumno_horario_salida = models.TimeField()
    alumno = models.ForeignKey(TblAlumno, on_delete=models.CASCADE)

    class Meta:
        db_table = 'tbl_alumno_horario'


class TblApoderado(models.Model):
    apoderado_id = models.AutoField(primary_key=True)
    apoderado_nombre = models.CharField(max_length=255)
    apoderado_apellido = models.CharField(max_length=255)
    apoderado_telefono = models.CharField(max_length=255)
    apoderado_documento_identidad = models.CharField(max_length=20, blank=True, null=True)
    parentesco = models.ForeignKey('TblParentesco', on_delete=models.CASCADE)

    class Meta:
        db_table = 'tbl_apoderado'


class TblCargo(models.Model):
    cargo_id = models.AutoField(primary_key=True)
    cargo_nombre = models.CharField(max_length=45)
    cargo_sueldo = models.FloatField()

    class Meta:
        db_table = 'tbl_cargo'


class TblColegio(models.Model):
    colegio_id = models.AutoField(primary_key=True)
    colegio_nombre = models.CharField(max_length=255)
    zona = models.ForeignKey('TblZona', on_delete=models.CASCADE)
    colegio_direccion = models.CharField(max_length=255)
    colegio_telefono = models.CharField(max_length=20)
    colegio_contacto = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = 'tbl_colegio'


class TblEmpleado(models.Model):
    empleado_id = models.AutoField(primary_key=True)
    empleado_nombre = models.CharField(max_length=255)
    empleado_apellido = models.CharField(max_length=255)
    empleado_telefono = models.CharField(max_length=45)
    supervisor = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)
    cargo = models.ForeignKey(TblCargo, on_delete=models.CASCADE)
    tbl_vehiculo_vehiculo = models.ForeignKey('TblVehiculo', on_delete=models.CASCADE)

    class Meta:
        db_table = 'tbl_empleado'


class TblEmpleadoHonorario(models.Model):
    empleado_honorario_id = models.AutoField(primary_key=True)
    empleado_honorario_monto = models.FloatField()
    empleado_honorario_fecha = models.DateField()
    tbl_empleado_empleado = models.ForeignKey(TblEmpleado, on_delete=models.CASCADE)

    class Meta:
        db_table = 'tbl_empleado_honorario'


class TblFormaPago(models.Model):
    forma_pago_id = models.AutoField(primary_key=True)
    forma_pago_nombre = models.CharField(max_length=45)
    forma_pago_referencia = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        db_table = 'tbl_forma_pago'


class TblGrado(models.Model):
    grado_id = models.AutoField(primary_key=True)
    grado_nombre = models.CharField(max_length=50)
    grado_nivel = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        db_table = 'tbl_grado'


class TblMovilidad(models.Model):
    movilidad_id = models.AutoField(primary_key=True)
    movilidad_tipo_servicio = models.CharField(max_length=45)
    movilidad_turno = models.CharField(max_length=45)
    movilidad_seccion = models.CharField(max_length=45)
    movilidad_docente = models.CharField(max_length=255)
    movilidad_pago = models.FloatField()
    colegio = models.ForeignKey(TblColegio, on_delete=models.CASCADE)
    apoderado = models.ForeignKey(TblApoderado, on_delete=models.CASCADE)
    grado = models.ForeignKey(TblGrado, on_delete=models.CASCADE)
    vehiculo = models.ForeignKey('TblVehiculo', on_delete=models.CASCADE)
    alumno = models.ForeignKey(TblAlumno, on_delete=models.CASCADE)

    class Meta:
        db_table = 'tbl_movilidad'


class TblMovilidadPago(models.Model):
    movilidad_pago_id = models.AutoField(primary_key=True)
    movilidad_pago_fecha = models.DateField()
    movilidad_pago_monto = models.FloatField()
    movilidad = models.ForeignKey(TblMovilidad, on_delete=models.CASCADE)
    forma_pago = models.ForeignKey(TblFormaPago, on_delete=models.CASCADE)

    class Meta:
        db_table = 'tbl_movilidad_pago'


class TblMovilidadRuta(models.Model):
    movilidad_ruta_id = models.AutoField(primary_key=True)
    movilidad_ruta_direccion = models.CharField(max_length=255)
    movilidad_ruta_hora_recojo = models.TimeField(blank=True, null=True)
    movilidad_ruta_hora_retorno = models.TimeField(blank=True, null=True)
    movilidad = models.ForeignKey(TblMovilidad, on_delete=models.CASCADE)

    class Meta:
        db_table = 'tbl_movilidad_ruta'


class TblParentesco(models.Model):
    parentesco_id = models.AutoField(primary_key=True)
    parentesco_nombre = models.CharField(max_length=45)

    class Meta:
        db_table = 'tbl_parentesco'


class TblTipoMantenimiento(models.Model):
    tipo_mantenimiento_id = models.AutoField(primary_key=True)
    tipo_mantenimiento_nombre = models.CharField(max_length=45)
    tipo_mantenimiento_descripcion = models.CharField(max_length=100)

    class Meta:
        db_table = 'tbl_tipo_mantenimiento'


class TblVehiculo(models.Model):
    vehiculo_id = models.AutoField(primary_key=True)
    vehiculo_placa = models.CharField(max_length=20)
    vehiculo_km = models.FloatField()
    vehiculo_marca = models.CharField(max_length=45)
    vehiculo_modelo = models.CharField(max_length=45)

    class Meta:
        db_table = 'tbl_vehiculo'


class TblVehiculoDocumento(models.Model):
    vehiculo_documento = models.AutoField(primary_key=True)
    vehiculo_documento_nombre = models.CharField(max_length=45)
    vehiculo_documento_fecha_vencimiento = models.DateField()
    tbl_vehiculo_vehiculo = models.ForeignKey(TblVehiculo, on_delete=models.CASCADE)

    class Meta:
        db_table = 'tbl_vehiculo_documento'


class TblVehiculoGasto(models.Model):
    vehiculo_gasto_id = models.AutoField(primary_key=True)
    vehiculo_gasto_descripcion = models.TextField(blank=True, null=True)
    vehiculo_gasto_monto = models.FloatField(blank=True, null=True)
    vehiculo_gasto_fecha = models.DateField(blank=True, null=True)
    vehiculo = models.ForeignKey(TblVehiculo, on_delete=models.CASCADE)
    tipo_gasto_tipo_gasto = models.ForeignKey('TipoGasto', on_delete=models.CASCADE)

    class Meta:
        db_table = 'tbl_vehiculo_gasto'


class TblVehiculoMantenimiento(models.Model):
    vehiculo_mantenimiento_id = models.AutoField(primary_key=True)
    vehiculo_mantenimiento_fecha = models.DateField()
    vehiculo_mantenimiento_observacion = models.TextField(blank=True, null=True)
    vehiculo_mantenimiento_fecha_futura = models.DateField()
    vehiculo_mantenimiento_km = models.FloatField()
    tipo_mantenimiento = models.ForeignKey(TblTipoMantenimiento, on_delete=models.CASCADE)
    vehiculo = models.ForeignKey(TblVehiculo, on_delete=models.CASCADE)

    class Meta:
        db_table = 'tbl_vehiculo_mantenimiento'



class TblZona(models.Model):
    zona_id = models.AutoField(primary_key=True)
    zona_nombre = models.CharField(max_length=255)

    class Meta:
        db_table = 'tbl_zona'


class TipoGasto(models.Model):
    tipo_gasto_id = models.AutoField(primary_key=True)
    tipo_gasto_nombre = models.CharField(max_length=255)

    class Meta:
        db_table = 'tipo_gasto'