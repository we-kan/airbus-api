# Generated by Django 2.1.7 on 2019-03-07 07:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('airport', '0001_initial'),
        ('flight', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FlightRoute',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
                ('flight_number', models.CharField(max_length=50)),
                ('end_location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='arrived_at', to='airport.Airport')),
                ('start_location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='departed_from', to='airport.Airport')),
            ],
        ),
        migrations.CreateModel(
            name='JourneyInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('journey_date', models.DateField()),
                ('flight', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flight.Flight')),
                ('flight_route', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flight_route.FlightRoute')),
            ],
        ),
    ]
