# Generated by Django 3.2.6 on 2021-09-06 05:08

from django.db import migrations
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('Library', '0006_remove_author_country'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='country',
            field=django_countries.fields.CountryField(default=0, max_length=2),
            preserve_default=False,
        ),
    ]
