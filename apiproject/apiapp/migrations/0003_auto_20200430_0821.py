# Generated by Django 3.0.5 on 2020-04-30 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apiapp', '0002_auto_20200430_0817'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hamburguesa',
            name='ingredientes',
            field=models.ManyToManyField(blank=True, to='apiapp.Ingrediente'),
        ),
    ]
