# Generated by Django 5.0.7 on 2024-07-13 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_montag_nshr'),
    ]

    operations = [
        migrations.CreateModel(
            name='place',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place_name', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='employee',
            name='places',
            field=models.ManyToManyField(blank=True, null=True, to='main.place'),
        ),
    ]
