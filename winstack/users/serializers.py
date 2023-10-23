from rest_framework import serializers
from .models import CustomUser, Event, StickyNote

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:        
        model = CustomUser        
        fields = (
            'id', 'username', 'email', 'password', 'bio', 'birthdate', 
            'linkedin_profile', 'github_username', 'is_organiser', 'is_attendee'
        )
        extra_kwargs = {'password': {'write_only': True}}

def create(self, validated_data):
    password = validated_data.pop('password')

    # Retrieve the flags if they exist and remove them from validated_data
    is_organiser = validated_data.pop('is_organiser', None)
    is_attendee = validated_data.pop('is_attendee', None)
    
    user = CustomUser(**validated_data)
    if is_organiser is not None:  # Check if the flag exists in validated_data
        user.is_organiser = is_organiser
    if is_attendee is not None:
        user.is_attendee = is_attendee

    user.set_password(password)
    user.save()
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

