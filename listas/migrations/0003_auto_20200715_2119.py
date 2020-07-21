# Generated by Django 3.0.8 on 2020-07-16 02:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('listas', '0002_auto_20200709_0411'),
    ]

    operations = [
        migrations.AddField(
            model_name='bodegas',
            name='total',
            field=models.IntegerField(default=0),
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.IntegerField(default=0, unique=True)),
                ('nombre', models.CharField(max_length=100, verbose_name='NOMBRE')),
                ('categoria', models.CharField(choices=[('riester', 'Riester'), ('genericos', 'Genericos'), ('otras marcas', 'Otras Marcas')], max_length=18, verbose_name='Categoria')),
                ('descripcion', models.TextField(blank=True, max_length=2000, null=True, verbose_name='DESCRIPCION')),
                ('stockinicial', models.IntegerField(default=0)),
                ('entradas', models.IntegerField(default=0)),
                ('salidas', models.IntegerField(default=0)),
                ('total', models.IntegerField(default=0)),
                ('por', models.DecimalField(decimal_places=2, default=0.0, max_digits=9)),
                ('final', models.IntegerField(default=0)),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='producto/%Y/%m', verbose_name='Imagen')),
                ('autor', models.ForeignKey(blank=True, max_length=400, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Producto',
                'verbose_name_plural': 'Productos',
                'ordering': ['id'],
            },
        ),
    ]