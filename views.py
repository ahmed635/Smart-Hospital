from django.contrib import messages
from django.shortcuts import redirect, render
from accounts.models import Patient, WorkstationNurse, Doctor
from .models import PatientParameter
from datetime import date


# Create your views here.


def patient(request, pat_id):
    if request.user.is_authenticated:
        context = None
        if request.user.id == pat_id:
            # patient want to see his/her parameters
            if Patient.objects.filter(user=request.user).exists():
                patient = Patient.objects.get(user=request.user)
                if PatientParameter.objects.filter(patient=patient).exists():
                    patient_parameter = PatientParameter.objects.filter(patient=patient).order_by('-id')[0]
                    context = {
                        'patient': patient,
                        'patient_parameter': patient_parameter,
                        'no_parameters': False,
                        'is_doctor': False  
                    }
                else:
                    messages.info(request, 'There is no measured parameters for this patient')
                    context = {
                        'patient': patient,
                        'no_parameters': True,
                        'is_doctor': False
                    }
            return render(request, 'patient/patient.html', context)
        else:
            # doctor want to see patient parameters
            if Doctor.objects.filter(user=request.user).exists():
                patient = Patient.objects.get(user_id=pat_id)
                if PatientParameter.objects.filter(patient=patient).exists():
                    patient_parameter = PatientParameter.objects.filter(patient=patient).order_by('id')[0]
                    context = {
                        'patient': patient,
                        'patient_parameter': patient_parameter,
                        'no_parameters': False,
                        'is_doctor': True
                    }
                else:
                    messages.info(request, 'There is no measured parameters for this patient')
                    context = {
                        'patient': patient,
                        'no_parameters': True,
                        'is_doctor':True,
                        'patient_parameter': patient_parameter
                    }
            return render(request, 'patient/patient.html', context)
    else:
        return redirect('_404')


def charts(request,chart_id):
    if request.user.is_authenticated:
        context = None

        # get patient object
        patient = Patient.objects.get(user_id=chart_id)

        # check type of user
        if PatientParameter.objects.filter(patient=patient).exists():
            patient_parameter = PatientParameter.objects.filter(patient=patient,date_in=date.today())
            if WorkstationNurse.objects.filter(user=request.user).exists():
                context = {
                    'patient': patient,
                    'patient_parameter': patient_parameter,
                    'is_patient': False,
                    'is_workstation_nurse': True,
                    'is_doctor': False,
                    'no_chart': False
                }
            elif Doctor.objects.filter(user=request.user).exists():
                context = {
                    'patient': patient,
                    'patient_parameter': patient_parameter,
                    'is_patient': False,
                    'is_workstation_nurse': False,
                    'is_doctor': True,
                    'no_chart': False
                }
            else:
                context = {
                    'patient': patient,
                    'patient_parameter': patient_parameter,
                    'is_patient': True,
                    'is_workstation_nurse': False,
                    'is_doctor': False,
                    'no_chart': False
                }
        else:
            # no parameters for this patient
            if WorkstationNurse.objects.filter(user=request.user).exists():
                context = {
                    'patient': patient,
                    'is_patinet': False,
                    'is_workstation_nurse': True,
                    'is_doctor': False,
                    'no_chart': True
                }
            elif Doctor.objects.filter(user=request.user).exists():
                context = {
                    'patient': patient,
                    'is_patinet': False,
                    'is_workstation_nurse': False,
                    'is_doctor': True,
                    'no_chart': True
                }
            else:
                context = {
                    'patient': patient,
                    'is_patient': True,
                    'is_workstation_nurse': False,
                    'is_doctor': False,
                    'no_chart': True
                }
                messages.info(request, 'There is no charts for this patient')
        return render(request, 'patient/charts.html', context)
    else: 
        return redirect('_404')
    
