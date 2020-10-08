# Generated by Django 3.1.1 on 2020-10-08 11:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TODO', '0009_auto_20201008_1349'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='completed',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='todo',
            name='title',
            field=models.CharField(blank=True, max_length=250),
        ),
        migrations.AlterField(
            model_name='todo',
            name='created',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 10, 8, 14, 11, 12, 90955), verbose_name='Дата регистрации'),
        ),
    ]