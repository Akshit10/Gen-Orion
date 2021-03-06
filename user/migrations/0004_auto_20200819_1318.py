# Generated by Django 2.1.7 on 2020-08-19 13:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('user', '0003_nodemcu_table'),
    ]

    operations = [
        migrations.CreateModel(
            name='device_table',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('device_id', models.IntegerField(unique=True)),
                ('device_name', models.CharField(max_length=40)),
                ('value', models.TextField()),
                ('create_date', models.DateTimeField()),
                ('update_date', models.DateTimeField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='sensor_table',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sensor_id', models.IntegerField(unique=True)),
                ('sensor_name', models.CharField(max_length=40)),
                ('value', models.TextField()),
                ('create_date', models.DateTimeField()),
                ('update_date', models.DateTimeField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='Sensors',
        ),
    ]
