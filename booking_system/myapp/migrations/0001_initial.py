# Generated by Django 5.0.4 on 2024-04-20 07:58

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Building',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('building_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('room_name', models.CharField(max_length=50)),
                ('building', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.building')),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('start_date', models.DateTimeField()),
                ('start_hour', models.TimeField(default='08:00:00')),
                ('end_hour', models.TimeField(default='10:00:00')),
                ('marge', models.IntegerField(null=True)),
                ('user', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.room')),
            ],
        ),
    ]
