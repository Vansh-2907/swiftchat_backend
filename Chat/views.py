from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Room, Message
from .serializers import MessageSerializer

@api_view(['GET'])
def get_messages(request, room_name):
    room, _ = Room.objects.get_or_create(name=room_name)
    messages = Message.objects.filter(room=room).order_by('timestamp')
    return Response(MessageSerializer(messages, many=True).data)

@api_view(['POST'])
def send_message(request):
    room_name = request.data.get('room')
    text = request.data.get('text')
    room, _ = Room.objects.get_or_create(name=room_name)
    Message.objects.create(room=room, text=text)
    return Response({'status': 'Message sent'})
