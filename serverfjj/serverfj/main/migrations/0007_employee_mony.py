# Generated by Django 5.0.7 on 2024-07-14 16:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_employee_mony'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='mony',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='main.employee_mony'),
        ),
    ]
