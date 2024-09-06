# Generated by Django 5.1 on 2024-09-03 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Core', '0004_annualplan_activity_casualplan_activity'),
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('deadline', models.DateField()),
                ('assigned_person', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='unit',
            name='position_id',
            field=models.CharField(default='dkmfk', max_length=30, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='workunit',
            name='position_id',
            field=models.CharField(default='sndmnd', max_length=30, unique=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='unit',
            name='name',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]