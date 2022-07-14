from django.contrib import admin
from .models import HoursOfMedicationNurse, Medication, TaskList
# Register your models here.

admin.site.register(HoursOfMedicationNurse)
admin.site.register(Medication)
admin.site.register(TaskList)
