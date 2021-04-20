# Generated by Django 3.1.7 on 2021-04-14 02:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Entidad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Encuestavacunacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=150)),
                ('apellido', models.CharField(max_length=150)),
                ('vacunado', models.BooleanField(null=True)),
                ('edad', models.IntegerField(null=True)),
                ('entidad', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='encuesta.entidad')),
            ],
        ),
    ]
