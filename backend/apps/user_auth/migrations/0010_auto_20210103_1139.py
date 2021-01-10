# Generated by Django 3.1.2 on 2021-01-03 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_auth', '0009_auto_20210102_1248'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'ordering': ('-pk',), 'verbose_name': 'user', 'verbose_name_plural': 'users'},
        ),
        migrations.RemoveField(
            model_name='user',
            name='avatar',
        ),
        migrations.AddField(
            model_name='user',
            name='date_of_birth',
            field=models.DateField(blank=True, null=True, verbose_name='Дата рождения'),
        ),
        migrations.AddField(
            model_name='user',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='photo/'),
        ),
    ]