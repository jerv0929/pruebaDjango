# Generated by Django 4.0.1 on 2022-01-21 03:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0003_producto_cantidad'),
    ]

    operations = [
        migrations.CreateModel(
            name='imagene',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('referenciaFk', models.CharField(max_length=7)),
                ('imagen', models.CharField(max_length=200)),
            ],
        ),
    ]