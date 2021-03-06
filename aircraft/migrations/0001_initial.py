# Generated by Django 2.1.7 on 2019-03-07 07:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AirCraft',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='AirCraftInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fuel_capacity_right_wing', models.IntegerField()),
                ('fuel_capacity_left_wing', models.IntegerField()),
                ('gross_weight', models.IntegerField()),
                ('harness_length', models.IntegerField()),
                ('atmospheric_pressure', models.IntegerField()),
                ('room_temperature', models.IntegerField()),
                ('aircraft', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='aircraft.AirCraft')),
            ],
        ),
    ]
