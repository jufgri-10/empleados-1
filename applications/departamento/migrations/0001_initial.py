# Generated by Django 3.0.6 on 2020-07-14 03:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Departamento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Nombre')),
                ('shor_name', models.CharField(max_length=20, unique=True, verbose_name='Nombre Corto')),
                ('anulate', models.BooleanField(default=False, verbose_name='Anulado')),
            ],
            options={
                'verbose_name': 'Departamento',
                'verbose_name_plural': 'Areas de la Empresa',
                'ordering': ['name'],
                'unique_together': {('name', 'shor_name')},
            },
        ),
    ]