# Generated by Django 4.1.3 on 2022-11-29 14:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employeemodel',
            name='position',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='employees.positionmodel'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='employeemodel',
            name='subdivision',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='employees.subdivisionmodel'),
            preserve_default=False,
        ),
    ]
