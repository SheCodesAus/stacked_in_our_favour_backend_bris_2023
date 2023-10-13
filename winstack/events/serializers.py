from rest_framework import serializers
from django.apps import apps


class StickyNoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = apps.get_model('events.StickyNote')
        fields = '__all__'


class EventSerializer(serializers.ModelSerializer):
    class Meta: 
        model = apps.get_model('events.Event')
        fields = '__all__'



