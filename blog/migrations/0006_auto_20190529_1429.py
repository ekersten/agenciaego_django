# Generated by Django 2.2.1 on 2019-05-29 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20190529_1222'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpage',
            name='likes',
            field=models.PositiveIntegerField(default=1349),
        ),
    ]
