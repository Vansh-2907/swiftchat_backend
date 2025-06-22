# Create your models here.
from django.db import models

class Room(models.Model):
    name = models.CharField(max_length=255, unique=True)

class Message(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    text = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
