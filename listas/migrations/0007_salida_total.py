# Generated by Django 3.0.8 on 2020-07-17 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listas', '0006_auto_20200716_0118'),
    ]

    operations = [
        migrations.AddField(
            model_name='salida',
            name='total',
            field=models.IntegerField(default=0),
        ),
    ]