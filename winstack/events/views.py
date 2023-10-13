from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Event
from .serializers import EventSerializer
from django.http import Http404
from rest_framework import status

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
            return Response(serializer.data, status=status.HTTP_202_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Handle single-event view
class EventDetail(APIView):
    
    def get_object(self, pk):
        try:
            return Event.objects.get(pk=pk)
        except Event.DoesNotExist:
            raise Http404
    
    def get(self,request, pk):
        event = self.get_object(pk)
        serializer = EventSerializer(event)
        return Response(serializer.data)
    
    def put(self, request, pk):
        event = self.get_object(pk)
        serializer = EventSerializer(event, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)