# Generated by Django 3.0.8 on 2020-09-12 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TODO', '0004_auto_20200913_0014'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
