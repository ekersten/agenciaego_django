# Generated by Django 2.2.1 on 2019-05-28 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('behance', '0002_auto_20190527_1553'),
    ]

    operations = [
        migrations.AddField(
            model_name='behanceprojectpage',
            name='featured_in_services',
            field=models.BooleanField(default=False),
        ),
    ]
