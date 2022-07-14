from django.shortcuts import redirect, render
from django.http import JsonResponse
from accounts.models import Patient, WorkstationNurse
from patient.models import PatientParameter
import pyrebase
from django.contrib import messages

# connect to firebase
config = { 
    'apiKey': "AIzaSyC8ik1oDX37iSXjsk4DZlMX4c8UDJv-OGU",
    'authDomain': "digital-hospital-b00fa.firebaseapp.com",
    'databaseURL': "https://digital-hospital-b00fa-default-rtdb.europe-west1.firebasedatabase.app",
    'projectId': "digital-hospital-b00fa",
    'storageBucket': "digital-hospital-b00fa.appspot.com",
    'messagingSenderId': "284435340965",
    'appId': "1:284435340965:web:ab09f5cfc5b53793b2774c",
    'measurementId': "G-1YNSNCH2EW"
}
firebase = pyrebase.initialize_app(config)
authe = firebase.auth()
db = firebase.database()


def getRealParameters(request):
    patient_parameters = db.child("UsersData").child('83Nvnsym3hVtVMR649yc0lLdl8u2').get().val()
    
    # get device id from server
    device_id = patient_parameters["device_id"]
    

    # check if device of userprofile is the same as device in firebase
    if Patient.objects.filter(device=device_id).exists():
        patient = Patient.objects.get(device=device_id)
        
        # storing the parameters in the model
        parameters = PatientParameter(
            patient=patient,
            sys_pressure=patient_parameters["sys pressure"],
            dia_pressure = patient_parameters["dya pressure"],
            HR = patient_parameters["Heart Rate"],
            spo2 = patient_parameters["SPO2"],
            temp = patient_parameters["body temperature"],
            env_temp = patient_parameters["ambient"]
            )
        parameters.save()
        return JsonResponse({
            'patient_parameters': patient_parameters})
    else:
        # if device in firebase not in patient model
        messages.error(request, 'Check device id in firebase')
        return JsonResponse({'patient_parameters': patient_parameters})
    

# Create your views here.
def workstation_nurse(request):
    context = None
    if request.user.is_authenticated:
        if WorkstationNurse.objects.filter(user=request.user).exists():
            nurse = WorkstationNurse.objects.get(user=request.user)
            patient_parameters = db.child("UsersData").child('83Nvnsym3hVtVMR649yc0lLdl8u2').get().val()
            firebase_patient_id = patient_parameters["device_id"]
            patients = Patient.objects.filter(w_nurse=nurse)
            context = {
                'patients': patients,
                'firebase_patient_id': firebase_patient_id
            }
        else:
            messages.error(request, 'There is no patients asigned to this nurse')
        return render(request, 'workstation_nurse/nurse.html', context)
    else:
        return redirect('_404')
    
    

