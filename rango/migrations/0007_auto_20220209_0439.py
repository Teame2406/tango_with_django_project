# Generated by Django 2.2.26 on 2022-02-09 04:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0006_auto_20220209_0427'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='likes',
            field=models.IntegerField(default=32),
        ),
        migrations.AlterField(
            model_name='category',
            name='views',
            field=models.IntegerField(default=64),
        ),
    ]
