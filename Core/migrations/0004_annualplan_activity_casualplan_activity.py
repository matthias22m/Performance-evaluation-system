# Generated by Django 5.1 on 2024-08-31 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Core', '0003_remove_characterevaluation_behavior_description_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='annualplan',
            name='activity',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='casualplan',
            name='activity',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
