# Generated by Django 3.1.2 on 2021-01-02 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_auth', '0003_auto_20210102_1206'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_staff',
            field=models.BooleanField(default=False, verbose_name='staff status'),
        ),
    ]