# Generated by Django 4.2.3 on 2023-10-27 14:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0006_event_finishdate_event_startdate_alter_event_creator_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='finishDate',
        ),
        migrations.RemoveField(
            model_name='event',
            name='startDate',
        ),
    ]
