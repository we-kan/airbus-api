# Generated by Django 2.1.7 on 2019-03-07 05:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flight_route', '0002_auto_20190307_0557'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flightroute',
            name='flight_number',
            field=models.CharField(max_length=50),
        ),
    ]
