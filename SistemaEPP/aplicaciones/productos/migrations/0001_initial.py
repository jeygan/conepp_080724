# Generated by Django 5.0.6 on 2024-07-06 23:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('trabajadores', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Productos',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(blank=True, max_length=255, null=True, verbose_name='Nombre')),
                ('descripcion', models.CharField(blank=True, max_length=255, null=True, verbose_name='Descripcion')),
                ('cantidad', models.IntegerField(blank=True, null=True, unique=True)),
                ('tipo', models.CharField(blank=True, max_length=255, null=True, verbose_name='Tipo')),
                ('marca', models.CharField(blank=True, max_length=255, null=True, verbose_name='Marca')),
            ],
            options={
                'verbose_name': 'Producto',
                'verbose_name_plural': '1.Productos',
                'db_table': 'Productos',
                'permissions': [],
            },
        ),
        migrations.CreateModel(
            name='AsignacionDeProductos',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('fecha_asignacion', models.DateField(blank=True, null=True, verbose_name='Fecha de Asignacion')),
                ('fecha_devolucion', models.DateField(blank=True, null=True, verbose_name='Fecha de Devolucion')),
                ('estado', models.BooleanField(default=False)),
                ('trabajador', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='trabajadores.trabajadores')),
            ],
            options={
                'verbose_name': 'AsignacionDeProducto',
                'verbose_name_plural': '2.AsignacionDeProductos',
                'db_table': 'AsignacionDeProductos',
                'permissions': [],
            },
        ),
    ]
