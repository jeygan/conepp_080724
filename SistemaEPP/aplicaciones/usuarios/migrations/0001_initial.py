# Generated by Django 5.0.6 on 2024-07-06 23:40

import aplicaciones.usuarios.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuarios',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=200, unique=True, verbose_name='Username')),
                ('nombres', models.CharField(blank=True, max_length=200, null=True, verbose_name='Nombres')),
                ('apellidos', models.CharField(blank=True, max_length=200, null=True, verbose_name='Apellidos')),
                ('cedula', models.IntegerField(blank=True, null=True, unique=True)),
                ('activo', models.BooleanField(default=True)),
                ('is_superuser', models.BooleanField(default=False)),
                ('admin', models.BooleanField(default=False)),
                ('fecha_nacimiento', models.DateField(blank=True, null=True, verbose_name='Fecha de nacimiento')),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('ultimo_ingreso', models.DateTimeField(auto_now=True, verbose_name='fecha ultimo ingreso')),
                ('direccion', models.CharField(blank=True, default='Desconocido', max_length=100, null=True, verbose_name='Direccion')),
                ('imagenPerfil', models.ImageField(blank=True, default='media/perfil/default.png', max_length=200, null=True, upload_to=aplicaciones.usuarios.models.foto_perfil_usuarios, verbose_name='Imagen de Perfil')),
                ('rol', models.CharField(choices=[('administrador', 'Administrador'), ('profesor', 'Profesor'), ('estudiante', 'Estudiante')], default='estudiante', max_length=150, verbose_name='Rol')),
                ('genero', models.CharField(choices=[('m', 'Masculino'), ('f', 'Femenino')], default='m', max_length=150, null=True, verbose_name='Genero')),
                ('nacionalidad', models.CharField(choices=[('v', 'V'), ('e', 'E')], default='V', max_length=150, null=True, verbose_name='Nacionalidad')),
                ('telefono', models.CharField(blank=True, default='', max_length=50, null=True, verbose_name='Telefono')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'Usuario',
                'verbose_name_plural': 'Usuarios',
                'db_table': 'Usuarios',
                'permissions': [],
            },
        ),
    ]
