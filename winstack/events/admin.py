from django.contrib import admin
from .models import Event, StickyNote

class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'eventDatetime', 'isOpen')
    search_fields = ('title', 'creator')

class StickyNoteAdmin(admin.ModelAdmin):
    list_display = ('noteText', 'eventId', 'authorID', 'anonymous')
    list_filter = ('eventId', 'anonymous')
    
admin.site.register(Event)
admin.site.register(StickyNote)


