# Generated by Django 3.0.5 on 2020-04-30 21:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apiapp', '0004_remove_hamburguesa_ingredientes'),
    ]

    operations = [
        migrations.AddField(
            model_name='hamburguesa',
            name='ingredientes',
            field=models.ManyToManyField(blank=True, to='apiapp.Ingrediente'),
        ),
    ]
