from django.db import models
from accounts.models import Patient, WorkstationNurse, MedicationNurse




# total working hours of medication nurse
class HoursOfMedicationNurse(models.Model):
    ''' Stores the total working hours of medication nurse and the current date '''
    day_date = models.DateField("Date",auto_now=False ,auto_now_add=False)
    total_hours = models.CharField("Total Hours", max_length=30, null=True )
    m_nurse = models.ForeignKey( MedicationNurse, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.m_nurse.full_name} | Date: {self.day_date} | Total Hours: {self.total_hours}"

    
    class Meta:
        ordering = ['-day_date']
    

# Medication for each patient
class Medication(models.Model):
    ''' stores the standard form of writting medication '''
    medication_name = models.CharField("Medication Name", max_length=200, null=True)
    med_freq = models.CharField("Frequency", max_length=200, null=True)
    med_amount = models.CharField("Amount", max_length=200, null=True)
    med_strength = models.CharField("Strength", max_length=200, null=True)
    med_route = models.CharField("Route", max_length=200, null=True)
    med_refills = models.CharField("Refills", max_length=200, null=True)
    med_dispense = models.CharField("Dispense", max_length=200, null=True)
    med_time = models.TimeField("Time", null=True)
    med_start_date = models.DateField("Start Date", null=True)
    med_end_date = models.DateField("End Date", null=True)
    w_nurse = models.ForeignKey(WorkstationNurse, on_delete=models.CASCADE, null=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, null=True)
    m_nurse = models.ForeignKey(MedicationNurse, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.medication_name
    
    class Meta:
        ordering =['med_time']


# task list
class TaskList(models.Model):
    delivery_date = models.DateField("Date", auto_now_add=True, null=True)
    delivery_time = models.TimeField("Time", auto_now_add=True, null=True)

    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, null=True)
    m_nurse = models.ForeignKey(MedicationNurse, on_delete=models.CASCADE, null=True)
    medication = models.ForeignKey(Medication, on_delete=models.CASCADE, null=True)

    is_done = models.BooleanField("Is Done",default=False,null=True)
    def __str__(self):
        return f"patient name: {self.patient.full_name} | nurse name: {self.m_nurse.full_name} | delivery date: {self.delivery_date} | deliver time: {self.delivery_time}"

    class Meta:
        ordering = ['delivery_date']
        