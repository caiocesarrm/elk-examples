# Generated by Django 3.0.5 on 2020-08-31 04:42

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_auto_20200831_0433'),
    ]

    operations = [
        migrations.AlterField(
            model_name='processo',
            name='juizes',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=120, null=True), blank=True, null=True, size=None),
        ),
    ]