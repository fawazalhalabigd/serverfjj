# Generated by Django 5.0.7 on 2024-07-14 16:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_rename_employee_mony_employeemony_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='employeeMony',
            new_name='Mony',
        ),
    ]
