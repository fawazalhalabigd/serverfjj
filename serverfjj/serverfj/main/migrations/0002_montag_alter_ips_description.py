# Generated by Django 5.0.7 on 2024-07-13 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='montag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('s3r', models.CharField(max_length=255)),
            ],
        ),
        migrations.AlterField(
            model_name='ips',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]