from django.contrib import admin
from .models import Device, Patient, UserInfo, WorkstationNurse, MedicationNurse, Doctor, Manager, UserInfo



# Register your models here.
admin.site.register(WorkstationNurse)
admin.site.register(MedicationNurse)
admin.site.register(Doctor)
admin.site.register(Manager)
admin.site.register(Device)
admin.site.register(Patient)
admin.site.register(UserInfo)