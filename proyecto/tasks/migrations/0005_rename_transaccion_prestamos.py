# Generated by Django 4.2.9 on 2024-02-14 20:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0004_remove_inventario_en_prestamo'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Transaccion',
            new_name='Prestamos',
        ),
    ]