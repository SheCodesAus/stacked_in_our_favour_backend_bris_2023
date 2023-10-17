from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404
from rest_framework import status
from .models import Event, StickyNote
from .serializers import EventSerializer, StickyNoteSerializer, EventDetailSerializer

# Handle all events
class EventList(APIView):

    # Handles GET request
    def get(self,request):
        events = Event.objects.all()
        serializer = EventSerializer(events, many=True)
        return Response(serializer.data)
    
    # Handles POST request
    def post(self, request):
        serializer = EventSerializer(data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Handle single-event view
class EventDetail(APIView):
    
    def get_object(self, pk):
        try:
            event = Event.objects.get(pk=pk)
            return event
        except Event.DoesNotExist:
            raise Http404
    
    def get(self,request, pk):
        event = self.get_object(pk)
        serializer = EventDetailSerializer(event)
        return Response(serializer.data)
    
    def patch(self, request, pk):
        event = self.get_object(pk)
        serializer = EventDetailSerializer(event, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request, pk):
        event = self.get_object(pk)
        event.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
# Handle all sticky notes
class StickyNoteList(APIView):

    # Handles GET request
    def get(self,request):
        stickyNotes = StickyNote.objects.all()
        serializer = StickyNoteSerializer(stickyNotes, many=True)
        return Response(serializer.data)
    
    # Handles POST request
    def post(self, request):
        serializer = StickyNoteSerializer(data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class StickyNoteDetail(APIView):
    
    def get_object(self, pk):
        try:
            return StickyNote.objects.get(pk=pk)
        except StickyNote.DoesNotExist:
            raise Http404

    def patch(self, request, pk):
        stickyNote = self.get_object(pk)
        serializer = StickyNoteSerializer(stickyNote, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request, pk):
        stickyNote = self.get_object(pk)
        stickyNote.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)    
