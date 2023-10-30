# Generated by Django 4.2.3 on 2023-10-27 14:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0005_alter_event_creator_alter_event_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='finishDate',
            field=models.DateTimeField(default=datetime.datetime(2023, 10, 27, 15, 8, 35, 314858)),
        ),
        migrations.AddField(
            model_name='event',
            name='startDate',
            field=models.DateTimeField(default=datetime.datetime(2023, 10, 27, 14, 8, 35, 314851)),
        ),
        migrations.AlterField(
            model_name='event',
            name='creator',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='event',
            name='description',
            field=models.TextField(blank=True),
        ),
    ]