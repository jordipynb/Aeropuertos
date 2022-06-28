# Generated by Django 4.0.5 on 2022-06-28 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='role',
            field=models.CharField(choices=[('US', 'Usuario Comun'), ('AI', 'Administrador Instalaciones'), ('AA', 'Administrador Aeropuertos'), ('AR', 'Administrador Reparaciones'), ('AG', 'Administrador General')], default='US', max_length=2),
        ),
    ]
