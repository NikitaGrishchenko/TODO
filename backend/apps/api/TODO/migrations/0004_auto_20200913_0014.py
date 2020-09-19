# Generated by Django 3.0.8 on 2020-09-12 21:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('TODO', '0003_auto_20200912_2355'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='category', to='TODO.Category'),
        ),
    ]
