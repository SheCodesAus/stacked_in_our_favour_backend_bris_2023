from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Event
from .serializers import EventSerializer

class EventList(APIView):

    # Handles GET request
    def get(self,request):
        events = Event.objects.all()
        serializer = EventSerializer(events, many=True)
        return Response(serializer.data)
    
    # Handles POST request
    def post(self, request):
        serializer = EventSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)