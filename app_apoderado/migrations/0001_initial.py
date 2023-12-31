# Generated by Django 3.2 on 2023-06-25 03:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TblAlumno',
            fields=[
                ('alumno_id', models.AutoField(primary_key=True, serialize=False)),
                ('alumno_nombre', models.CharField(max_length=255)),
                ('alumno_apellido', models.CharField(max_length=255)),
                ('alumno_fecha_nacimiento', models.DateField(blank=True, null=True)),
                ('alumno_foto', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'tbl_alumno',
            },
        ),
        migrations.CreateModel(
            name='TblApoderado',
            fields=[
                ('apoderado_id', models.AutoField(primary_key=True, serialize=False)),
                ('apoderado_nombre', models.CharField(max_length=255)),
                ('apoderado_apellido', models.CharField(max_length=255)),
                ('apoderado_telefono', models.CharField(max_length=255)),
                ('apoderado_documento_identidad', models.CharField(blank=True, max_length=20, null=True)),
            ],
            options={
                'db_table': 'tbl_apoderado',
            },
        ),
        migrations.CreateModel(
            name='TblCargo',
            fields=[
                ('cargo_id', models.AutoField(primary_key=True, serialize=False)),
                ('cargo_nombre', models.CharField(max_length=45)),
                ('cargo_sueldo', models.FloatField()),
            ],
            options={
                'db_table': 'tbl_cargo',
            },
        ),
        migrations.CreateModel(
            name='TblColegio',
            fields=[
                ('colegio_id', models.AutoField(primary_key=True, serialize=False)),
                ('colegio_nombre', models.CharField(max_length=255)),
                ('colegio_direccion', models.CharField(max_length=255)),
                ('colegio_telefono', models.CharField(max_length=20)),
                ('colegio_contacto', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'tbl_colegio',
            },
        ),
        migrations.CreateModel(
            name='TblEmpleado',
            fields=[
                ('empleado_id', models.AutoField(primary_key=True, serialize=False)),
                ('empleado_nombre', models.CharField(max_length=255)),
                ('empleado_apellido', models.CharField(max_length=255)),
                ('empleado_telefono', models.CharField(max_length=45)),
                ('cargo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_apoderado.tblcargo')),
                ('supervisor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app_apoderado.tblempleado')),
            ],
            options={
                'db_table': 'tbl_empleado',
            },
        ),
        migrations.CreateModel(
            name='TblFormaPago',
            fields=[
                ('forma_pago_id', models.AutoField(primary_key=True, serialize=False)),
                ('forma_pago_nombre', models.CharField(max_length=45)),
                ('forma_pago_referencia', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'tbl_forma_pago',
            },
        ),
        migrations.CreateModel(
            name='TblGrado',
            fields=[
                ('grado_id', models.AutoField(primary_key=True, serialize=False)),
                ('grado_nombre', models.CharField(max_length=50)),
                ('grado_nivel', models.CharField(blank=True, max_length=45, null=True)),
            ],
            options={
                'db_table': 'tbl_grado',
            },
        ),
        migrations.CreateModel(
            name='TblMovilidad',
            fields=[
                ('movilidad_id', models.AutoField(primary_key=True, serialize=False)),
                ('movilidad_tipo_servicio', models.CharField(max_length=45)),
                ('movilidad_turno', models.CharField(max_length=45)),
                ('movilidad_seccion', models.CharField(max_length=45)),
                ('movilidad_docente', models.CharField(max_length=255)),
                ('movilidad_pago', models.FloatField()),
                ('alumno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_apoderado.tblalumno')),
                ('apoderado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_apoderado.tblapoderado')),
                ('colegio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_apoderado.tblcolegio')),
                ('grado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_apoderado.tblgrado')),
            ],
            options={
                'db_table': 'tbl_movilidad',
            },
        ),
        migrations.CreateModel(
            name='TblParentesco',
            fields=[
                ('parentesco_id', models.AutoField(primary_key=True, serialize=False)),
                ('parentesco_nombre', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'tbl_parentesco',
            },
        ),
        migrations.CreateModel(
            name='TblTipoMantenimiento',
            fields=[
                ('tipo_mantenimiento_id', models.AutoField(primary_key=True, serialize=False)),
                ('tipo_mantenimiento_nombre', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'tbl_tipo_mantenimiento',
            },
        ),
        migrations.CreateModel(
            name='TblVehiculo',
            fields=[
                ('vehiculo_id', models.AutoField(primary_key=True, serialize=False)),
                ('vehiculo_placa', models.CharField(max_length=20)),
                ('vehiculo_km', models.FloatField()),
                ('vehiculo_marca', models.CharField(max_length=45)),
                ('vehiculo_modelo', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'tbl_vehiculo',
            },
        ),
        migrations.CreateModel(
            name='TblZona',
            fields=[
                ('zona_id', models.AutoField(primary_key=True, serialize=False)),
                ('zona_nombre', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'tbl_zona',
            },
        ),
        migrations.CreateModel(
            name='TipoGasto',
            fields=[
                ('tipo_gasto_id', models.AutoField(primary_key=True, serialize=False)),
                ('tipo_gasto_nombre', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'tipo_gasto',
            },
        ),
        migrations.CreateModel(
            name='TblVehiculoMantenimiento',
            fields=[
                ('vehiculo_mantenimiento_id', models.AutoField(primary_key=True, serialize=False)),
                ('vehiculo_mantenimiento_fecha', models.DateField()),
                ('vehiculo_mantenimiento_observacion', models.TextField(blank=True, null=True)),
                ('vehiculo_mantenimiento_fecha_futura', models.DateField()),
                ('vehiculo_mantenimiento_km', models.FloatField()),
                ('tipo_mantenimiento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_apoderado.tbltipomantenimiento')),
                ('vehiculo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_apoderado.tblvehiculo')),
            ],
            options={
                'db_table': 'tbl_vehiculo_mantenimiento',
            },
        ),
        migrations.CreateModel(
            name='TblVehiculoGasto',
            fields=[
                ('vehiculo_gasto_id', models.AutoField(primary_key=True, serialize=False)),
                ('vehiculo_gasto_descripcion', models.TextField(blank=True, null=True)),
                ('vehiculo_gasto_monto', models.FloatField(blank=True, null=True)),
                ('vehiculo_gasto_fecha', models.DateField(blank=True, null=True)),
                ('tipo_gasto_tipo_gasto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_apoderado.tipogasto')),
                ('vehiculo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_apoderado.tblvehiculo')),
            ],
            options={
                'db_table': 'tbl_vehiculo_gasto',
            },
        ),
        migrations.CreateModel(
            name='TblVehiculoDocumento',
            fields=[
                ('vehiculo_documento', models.AutoField(primary_key=True, serialize=False)),
                ('vehiculo_documento_nombre', models.CharField(max_length=45)),
                ('vehiculo_documento_fecha_vencimiento', models.DateField()),
                ('tbl_vehiculo_vehiculo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_apoderado.tblvehiculo')),
            ],
            options={
                'db_table': 'tbl_vehiculo_documento',
            },
        ),
        migrations.CreateModel(
            name='TblMovilidadRuta',
            fields=[
                ('movilidad_ruta_id', models.AutoField(primary_key=True, serialize=False)),
                ('movilidad_ruta_direccion', models.CharField(max_length=255)),
                ('movilidad_ruta_hora_recojo', models.TimeField(blank=True, null=True)),
                ('movilidad_ruta_hora_retorno', models.TimeField(blank=True, null=True)),
                ('movilidad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_apoderado.tblmovilidad')),
            ],
            options={
                'db_table': 'tbl_movilidad_ruta',
            },
        ),
        migrations.CreateModel(
            name='TblMovilidadPago',
            fields=[
                ('movilidad_pago_id', models.AutoField(primary_key=True, serialize=False)),
                ('movilidad_pago_fecha', models.DateField()),
                ('movilidad_pago_monto', models.FloatField()),
                ('forma_pago', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_apoderado.tblformapago')),
                ('movilidad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_apoderado.tblmovilidad')),
            ],
            options={
                'db_table': 'tbl_movilidad_pago',
            },
        ),
        migrations.AddField(
            model_name='tblmovilidad',
            name='vehiculo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_apoderado.tblvehiculo'),
        ),
        migrations.CreateModel(
            name='TblEmpleadoHonorario',
            fields=[
                ('empleado_honorario_id', models.AutoField(primary_key=True, serialize=False)),
                ('empleado_honorario_monto', models.FloatField()),
                ('empleado_honorario_fecha', models.DateField()),
                ('tbl_empleado_empleado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_apoderado.tblempleado')),
            ],
            options={
                'db_table': 'tbl_empleado_honorario',
            },
        ),
        migrations.AddField(
            model_name='tblempleado',
            name='tbl_vehiculo_vehiculo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_apoderado.tblvehiculo'),
        ),
        migrations.AddField(
            model_name='tblcolegio',
            name='zona',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_apoderado.tblzona'),
        ),
        migrations.AddField(
            model_name='tblapoderado',
            name='parentesco',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_apoderado.tblparentesco'),
        ),
        migrations.CreateModel(
            name='TblAlumnoHorario',
            fields=[
                ('alumno_horario_id', models.AutoField(primary_key=True, serialize=False)),
                ('alumno_horario_dia', models.CharField(max_length=45)),
                ('alumno_horario_ingreso', models.TimeField()),
                ('alumno_horario_salida', models.TimeField()),
                ('alumno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_apoderado.tblalumno')),
            ],
            options={
                'db_table': 'tbl_alumno_horario',
            },
        ),
    ]
