# Generated by Django 3.0.5 on 2020-05-03 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apiapp', '0005_hamburguesa_ingredientes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hamburguesa',
            name='ingredientes',
            field=models.ManyToManyField(blank=True, related_name='hamburguesas', to='apiapp.Ingrediente'),
        ),
    ]
