# Generated by Django 5.1 on 2024-09-06 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Core', '0007_characterevaluation_result_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Activity',
        ),
        migrations.AlterField(
            model_name='characterevaluation',
            name='result',
            field=models.FloatField(default=0),
        ),
    ]
