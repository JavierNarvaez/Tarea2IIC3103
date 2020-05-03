# Generated by Django 3.0.5 on 2020-04-29 21:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hamburguesa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(default='', max_length=100)),
                ('precio', models.IntegerField(default='0')),
                ('descripcion', models.CharField(default='', max_length=100)),
                ('imagen', models.CharField(default='', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Ingrediente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(default='', max_length=100)),
                ('descripcion', models.CharField(default='', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Hamburguesa_Ingrediente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hamburguesa_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apiapp.Hamburguesa')),
                ('ingrediente_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apiapp.Ingrediente')),
            ],
        ),
    ]