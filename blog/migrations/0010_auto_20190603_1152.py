# Generated by Django 2.2.1 on 2019-06-03 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20190529_1654'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpage',
            name='likes',
            field=models.PositiveIntegerField(default=1146),
        ),
    ]