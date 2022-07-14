from django.db import models
from django.contrib.auth.models import User

# for phone number validation
from django.core.validators import RegexValidator


# workstation nurse model
class WorkstationNurse(models.Model):
    ''' stores the workstation nurse info. '''
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)  
    full_name = models.CharField("Full Name",max_length=150, null=True, default='')

    class Meta:
        ordering =['-full_name']

    def __str__(self):
        return self.user.username


# medication nurse model
class MedicationNurse(models.Model):
    ''' stores the Medication nurse info. '''
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)  
    full_name = models.CharField("Full Name",max_length=150, null=True, default='')

    class Meta:
        ordering =['-full_name']


    def __str__(self):
        return self.user.username


# doctor model
class Doctor(models.Model):
    ''' stores the doctor info. '''
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)  
    full_name = models.CharField("Full Name",max_length=150, null=True, default='')

    class Meta:
        ordering =['-full_name']

    def __str__(self):
        return self.user.username


# manager
class Manager(models.Model):
    ''' stores the Medication nurse info. '''
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)  
    full_name = models.CharField("Full Name",max_length=150, null=True, default='')

    class Meta:
        ordering =['-full_name']


    def __str__(self):
        return self.user.username


# device model
class Device(models.Model):
    ''' used to store the hardware device id '''
    device_id = models.CharField("Device ID", max_length=30, primary_key=True )

    def __str__(self) -> str:
        return self.device_id

    class Meta:
        ordering = ['-device_id']


# user_info model
class UserInfo(models.Model):
    ''' store the some information for all users '''
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    male = 'Male'
    female = 'Female'
    gender_choices = [
        (male, 'Male'),
        (female, 'Female'),
    ]
    gender = models.CharField("Gender",max_length=10, null=True, choices=gender_choices)
    birth_date = models.DateField("Birth of Date", null=True,auto_now=False, auto_now_add=False)
    phone_regex = RegexValidator(regex='^\+?1?\d{9,15}$', message="Phone number please")
    phone_number_1 = models.CharField("Phone number 1", validators=[phone_regex], max_length=17, blank=True)
    phone_number_2 = models.CharField("Phone number 2", validators=[phone_regex], max_length=17, blank=True)
    country = models.CharField("Country", max_length=20, null=True, blank=True, default='')
    city = models.CharField( "City", max_length=60, null= True, blank=True, default='')
    state = models.CharField("State",max_length=60 , null=True, default='')
    address_1 = models.CharField("Address line 1",max_length=200, null=True, default='')
    address_2 = models.CharField("Address line 2",max_length=200, null=True, default='')
    zip_code = models.CharField("ZIP/ Postal code",max_length=12, null=True, default='')

    def __str__(self):
        return self.user.username


# patient model
class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True) 
    full_name = models.CharField("Full Name",max_length=150, null=True, default='')
    start_date = models.DateField("Arrival Date",null=True,auto_now_add=True)
    has_hypertension = models.CharField("Hypertension", null=True ,max_length=150, default='')
    has_diabetes = models.CharField("Diabetes", null=True ,max_length=150, default='')
    has_covid = models.CharField("Covid", null=True ,max_length=150, default='')
    has_insurance = models.CharField("Insurance", null=True, max_length=150, default='')
    insurance_company = models.CharField("Insurance Company", null=True, max_length=150, default='')
    
    device = models.OneToOneField(Device, on_delete=models.prefetch_related_objects, null=True)
    
    w_nurse = models.ForeignKey(WorkstationNurse, on_delete=models.prefetch_related_objects, null=True)
    m_nurse = models.ForeignKey(MedicationNurse, on_delete=models.prefetch_related_objects, null=True)
    user_info = models.ForeignKey(UserInfo, on_delete=models.prefetch_related_objects, null=True)

    def __str__(self):
        return f"Patient Username: {self.user.username} | Device: {self.device} | Workstation Nurse: {self.w_nurse} | Medication Nurse: {self.m_nurse}"
    
    class Meta:
        ordering = ['-start_date']


