from django.db import models
from accounts.models import Patient
from django.contrib.auth.models import User


# model for room name
class Room(models.Model):
    patient = models.OneToOneField(Patient, on_delete=models.CASCADE, null=True)
    name = models.CharField("Room Name",max_length=1000, null=True, default='')

    def __str__(self):
        return f"{self.id}"


# model for message
class Message(models.Model):
    value = models.CharField("Message",max_length=1000000)
    date = models.DateField("Date", auto_now_add=True, null=True)
    time = models.TimeField("Time", auto_now_add=True, null=True)
    full_name = models.CharField("Full Name",max_length=150, null=True, default='')
    room = models.ForeignKey(Room, on_delete=models.prefetch_related_objects, null=True)
    user = models.ForeignKey(User, on_delete=models.prefetch_related_objects, null=True)

    def __str__(self) -> str:
        return f"Room {self.full_name} | Datetime: {self.date}"
