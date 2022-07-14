from django.db import models
from accounts.models import WorkstationNurse


# total working hours of workstation nurse
class HoursOfWorkstationNurse(models.Model):
    ''' Stores the total working hours of workstation nurse and the current date '''
    day_date = models.DateField("Date", auto_now=False, auto_now_add=False)
    total_hours = models.CharField("Total Hours", max_length=30, null=True )
    w_nurse = models.ForeignKey( WorkstationNurse, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.w_nurse.full_name} | Date: {self.day_date} | Total Hours: {self.total_hours}"
    
    class Meta:
        ordering = ['-day_date']
    
