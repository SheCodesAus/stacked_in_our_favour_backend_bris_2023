from rest_framework import serializers
from .models import CustomUser, Event, StickyNote

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:        
        model = CustomUser        
        fields = '__all__'
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = CustomUser.objects.create_user(**validated_data)
        # Option to include password hashing here // Not entirely sure how
        return user
    
class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'

    def create(self, validated_data):
        # Check if the user creating the event is an organiser
        if not self.context['request'].user.is_organiser:
            raise serializers.ValidationError("Only organisers can create events.")
        
        return super().create(validated_data)

class StickyNoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = StickyNote
        fields = '__all__'

