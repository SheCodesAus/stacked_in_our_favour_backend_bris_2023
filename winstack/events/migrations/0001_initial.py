# Generated by Django 4.2.6 on 2023-10-20 03:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True)),
                ('location', models.CharField(blank=True, max_length=50)),
                ('eventDatetime', models.DateTimeField()),
                ('openDate', models.DateTimeField()),
                ('closeDate', models.DateTimeField()),
                ('creator', models.CharField(max_length=200)),
                ('image', models.URLField(blank=True)),
                ('isOpen', models.BooleanField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='StickyNote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('noteText', models.CharField(max_length=250)),
                ('authorID', models.CharField(max_length=100)),
                ('anonymous', models.BooleanField()),
                ('eventId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='stickyNotes', to='events.event')),
            ],
        ),
    ]
