# Generated by Django 3.0.5 on 2020-04-30 21:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apiapp', '0003_auto_20200430_0821'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hamburguesa',
            name='ingredientes',
        ),
    ]
