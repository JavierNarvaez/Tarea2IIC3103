# Generated by Django 3.0.5 on 2020-05-03 20:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apiapp', '0006_auto_20200503_1938'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hamburguesa',
            name='descripcion',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='hamburguesa',
            name='imagen',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='hamburguesa',
            name='nombre',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='ingrediente',
            name='descripcion',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='ingrediente',
            name='nombre',
            field=models.CharField(max_length=100),
        ),
    ]
