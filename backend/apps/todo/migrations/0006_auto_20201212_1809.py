# Generated by Django 3.1.2 on 2020-12-12 15:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0005_auto_20201212_1306'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='priority_color',
            field=models.CharField(default='transparent', max_length=250),
        ),
        migrations.AlterField(
            model_name='todo',
            name='priority',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='priority', to='todo.priority'),
        ),
        migrations.AlterUniqueTogether(
            name='priority',
            unique_together={('name', 'color')},
        ),
    ]