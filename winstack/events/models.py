from django.db import models

class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    location = models.CharField(max_length=50, blank=True)
    eventDatetime = models.DateTimeField() #When event is happening, mandatory
    openDate =  models.DateTimeField() #Datetime when sticky notes can be posted, mandatory
    closeDate = models.DateTimeField() #Datetime when posting sticky notes end, mandatory
    creator = models.CharField(max_length=200)
    image = models.URLField(blank=True)
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