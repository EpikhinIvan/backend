# Generated by Django 4.2.7 on 2023-11-22 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eat',
            name='count',
            field=models.IntegerField(),
        ),
    ]
