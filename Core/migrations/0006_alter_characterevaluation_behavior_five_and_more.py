# Generated by Django 5.1 on 2024-09-04 20:57

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Core', '0005_activity_unit_position_id_workunit_position_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='characterevaluation',
            name='behavior_five',
            field=models.FloatField(default=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(4)]),
        ),
        migrations.AlterField(
            model_name='characterevaluation',
            name='behavior_four',
            field=models.FloatField(default=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(4)]),
        ),
        migrations.AlterField(
            model_name='characterevaluation',
            name='behavior_one',
            field=models.FloatField(default=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(4)]),
        ),
        migrations.AlterField(
            model_name='characterevaluation',
            name='behavior_six',
            field=models.FloatField(default=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(4)]),
        ),
        migrations.AlterField(
            model_name='characterevaluation',
            name='behavior_three',
            field=models.FloatField(default=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(4)]),
        ),
        migrations.AlterField(
            model_name='characterevaluation',
            name='behavior_two',
            field=models.FloatField(default=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(4)]),
        ),
        migrations.AlterField(
            model_name='characterevaluation',
            name='evaluation_date',
            field=models.DateField(auto_now=True),
        ),
    ]
