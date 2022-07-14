from django.shortcuts import redirect, render
from accounts.models import Patient, Device, Doctor
from comments.models import Comment
from patient.models import PatientParameter
from itertools import chain


# Create your views here.
def doctor(request):
    if request.user.is_authenticated:
        patients = Patient.objects.all()
        parameters = PatientParameter.objects.all()
        return render(request, 'doctor/doctor.html',{
            'patients': patients,
            'parameters': parameters,
        })
    else:
        return redirect('_404')
    
