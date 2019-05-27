# Generated by Django 2.2.1 on 2019-05-27 20:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0041_group_collection_permissions_verbose_name_plural'),
        ('core', '0002_projectdiscoverypage_servicespage'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
            ],
            options={
                'verbose_name': 'About Page',
                'verbose_name_plural': 'About Pages',
            },
            bases=('wagtailcore.page',),
        ),
        migrations.AlterModelOptions(
            name='servicespage',
            options={'verbose_name': 'Services Page', 'verbose_name_plural': 'Services Pages'},
        ),
    ]
