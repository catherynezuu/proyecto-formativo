# Generated by Django 4.2.9 on 2024-02-14 19:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0003_rename_fecha_hora_transaccion_fecha_prestamo_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='inventario',
            name='en_prestamo',
        ),
    ]