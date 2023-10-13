from rest_framework import serializers
from django.apps import apps

class EventSerializer(serializers.Serializer):
    class Meta: 
        model = apps.get_model('events.Event')
        fields = '__all__'
