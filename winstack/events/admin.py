from django import forms
from django.contrib import admin
from .models import Event, StickyNote
from users.models import CustomUser  # Import the CustomUser model

class EventAdminForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = '__all__'

    organizer = forms.ModelChoiceField(
        queryset=CustomUser.objects.filter(is_organiser=True),
        label='Organizer',
        required=True,
    )

class EventAdmin(admin.ModelAdmin):
    form = EventAdminForm
    list_display = ('title', 'isOpen')
    search_fields = ('title', 'creator')

class StickyNoteAdmin(admin.ModelAdmin):
    list_display = ('noteText', 'eventId', 'authorID', 'anonymous')
    list_filter = ('eventId', 'anonymous')

admin.site.register(Event, EventAdmin)
admin.site.register(StickyNote, StickyNoteAdmin)
