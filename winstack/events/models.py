from django.db import models
from users.models import CustomUser


class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    location = models.CharField(max_length=50, blank=True)
    creator = models.CharField(max_length=200)
    image = models.URLField(blank=True)
    start_datetime = models.DateTimeField("Start Date & Time", null=True, blank=True)
    finish_datetime = models.DateTimeField("Finish Date & Time", null=True, blank=True)
    isOpen = models.BooleanField(blank=True)


class StickyNote(models.Model):
    noteText = models.CharField(max_length=250)
    eventId = models.ForeignKey(
        'Event',
        on_delete=models.CASCADE,
        related_name = 'stickyNotes'
        )
    authorID = models.CharField(max_length=100)
    anonymous = models.BooleanField()