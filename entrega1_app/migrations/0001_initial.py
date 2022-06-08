# Generated by Django 4.0.4 on 2022-06-06 03:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Autorizaciones',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num_cuenta', models.IntegerField()),
                ('fecha_aut', models.DateField()),
                ('tipo_prod', models.CharField(max_length=40)),
                ('estado_trx', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Costos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_costo', models.CharField(max_length=40)),
                ('num_comercio', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Presentaciones',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num_cuenta', models.IntegerField()),
                ('fecha_pres', models.DateField()),
                ('tipo_prod', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Productos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_prod', models.CharField(max_length=40)),
                ('num_comercio', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Usuarios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('apellido', models.CharField(max_length=40)),
                ('nacimiento', models.DateField()),
                ('num_cuenta', models.IntegerField()),
                ('fecha_alta', models.DateField()),
            ],
        ),
    ]