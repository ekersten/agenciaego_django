# Generated by Django 2.2.1 on 2019-06-05 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_auto_20190605_1545'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpage',
            name='likes',
            field=models.PositiveIntegerField(default=1337),
        ),
    ]
