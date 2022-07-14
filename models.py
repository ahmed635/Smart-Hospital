from django.db import models
from accounts.models import Patient


# patient's parameters
class PatientParameter(models.Model):
    ''' to store the patient parameters '''
    HR = models.DecimalField( "Heart Rate",max_digits=5, decimal_places=2, default=0, null=True)
    spo2 = models.DecimalField("SPO2", max_digits=5, decimal_places=2, default=0, null=True)
    temp = models.DecimalField("Body Temperature",max_digits=5, decimal_places=2, default=0, null=True)
    env_temp = models.DecimalField("Environment Temperature",max_digits=5, decimal_places=2, default=0, null=True)
    sys_pressure = models.DecimalField("Systolic Pressure", max_digits=5, decimal_places=2, default=0, null=True)
    dia_pressure = models.DecimalField("Diastolic Pressure", max_digits=5, decimal_places=2, default=0, null=True)
    date_in = models.DateField("Date", auto_now_add=True, null=True)
    time_in = models.TimeField("Time", auto_now_add=True, null=True)
    
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, null=True)

    def __str__(self) -> str:
        # return str(self.time_in)
        return f"Patient Name : {self.patient.full_name} | Date : {self.date_in} | Time : {self.time_in}"

    class Meta:
        ordering = ['-date_in']