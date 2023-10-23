from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    is_organiser = models.BooleanField(default=False)
    is_attendee = models.BooleanField(default=True)  # Assuming most users will be attendees by default
    bio = models.TextField(blank=True)
    birthdate = models.DateField(null=True, blank=True)
    # profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    linkedin_profile = models.URLField(blank=True)
    github_username = models.CharField(max_length=50, blank=True)
    
    def __str__(self):
        return self.username
    

class Event(models.Model):
    organizer = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    date = models.DateTimeField()
    # Add more fields as needed

class StickyNote(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    content = models.TextField()
    # Add more fields as needed
