# Generated by Django 2.2.1 on 2019-06-04 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_auto_20190603_1152'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpage',
            name='likes',
            field=models.PositiveIntegerField(default=1399),
        ),
    ]
