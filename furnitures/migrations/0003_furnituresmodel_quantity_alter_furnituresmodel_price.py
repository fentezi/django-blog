# Generated by Django 4.2.4 on 2023-09-10 16:44

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('furnitures', '0002_alter_furnituresmodel_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='furnituresmodel',
            name='quantity',
            field=models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='furnituresmodel',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=6, validators=[django.core.validators.MinValueValidator(0)]),
        ),
    ]
