# Generated by Django 2.1 on 2018-08-19 15:20

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0003_auto_20180819_1515'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='rating',
            field=models.FloatField(null=True, validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(1)]),
        ),
    ]