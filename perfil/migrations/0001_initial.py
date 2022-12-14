# Generated by Django 4.1.4 on 2022-12-11 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='titulo')),
                ('desc', models.TextField(verbose_name='descripcion')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='fecha de creacion')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='fecha de actualizacion')),
            ],
            options={
                'verbose_name': 'Proyecto',
                'verbose_name_plural': 'Proyectos',
            },
        ),
    ]
