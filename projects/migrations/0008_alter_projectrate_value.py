# Generated by Django 4.0.4 on 2022-05-10 22:52

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0007_merge_0006_alter_projectrate_value_0006_commentreply'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectrate',
            name='value',
            field=models.FloatField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)]),
        ),
    ]
