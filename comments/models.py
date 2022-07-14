from django.db import models
from django.contrib.auth.models import User
from accounts.models import Patient

# Create your models here.
class Comment(models.Model):
    ''' store the comments of all users '''
    date_in = models.DateField("Date", auto_now_add=True, null=True)
    time_in = models.TimeField("Time", auto_now_add=True, null=True)
    comment = models.TextField("Comments", max_length=3000, null=True, default='comments')

    patient = models.ForeignKey(Patient, on_delete=models.prefetch_related_objects, null=True)
    user = models.ForeignKey(User, on_delete=models.prefetch_related_objects, null=True)

    def __str__(self) -> str:
        return f"The user:{self.user.username} | the patient: {self.patient.full_name} | the Date: {self.time_in} | the time: {self.time_in}"