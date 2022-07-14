from django.shortcuts import render, redirect
from django.shortcuts import HttpResponse
from .models import Medication, TaskList
from accounts.models import Patient,WorkstationNurse, MedicationNurse
from comments.models import Comment
from patient.models import PatientParameter
from django.contrib import messages
from datetime import date
import time

# create done view for medication nurse
def done(request):
    if request.method == 'POST':
        # get data using post
        patient = request.POST['patient']
        medication = request.POST['medication']

        # get patient and medication for these date
        pat = Patient.objects.get(pk=patient)
        med = Medication.objects.get(patient_id=patient, m_nurse=pat.m_nurse)
        
        current = time.localtime()
        
        # update the task list to be done
        task_list = TaskList.objects.get(patient_id=patient, delivery_date=date.today())
        task_list.is_done = True
        task_list.delivery_time = time.strftime("%H:%M", current)
        task_list.save()
        return HttpResponse('done')
    else:
        return redirect('_404')


# medication nurse view
def medication_nurse(request):
    if request.user.is_authenticated:
        medication = None
        context = None
        task_list = None
        if MedicationNurse.objects.filter(user=request.user).exists():
            medication_nurse = MedicationNurse.objects.get(user=request.user)
            medications = Medication.objects.filter(m_nurse=medication_nurse)
            date_today = date.today()
            for medication in medications:
                if medication.med_start_date < date_today and medication.med_end_date > date_today:                   
                    # to prevent duplications in task list
                    if TaskList.objects.filter(medication=medication,delivery_date=date_today).exists():
                        pass
                    else:
                        task_list = TaskList(
                            is_done=False,
                            patient=medication.patient,
                            m_nurse=medication.m_nurse,
                            medication_id=medication.id,
                            delivery_date=date.today(),
                        )
                        task_list.save()
                else:
                    messages.info(request, 'There is no patients asigned to this nurse')
            
            task_list = TaskList.objects.filter(m_nurse=medication_nurse, delivery_date=date_today)
            context = {
                'task_list': task_list,
                'date_today': date_today,
            }
        else:
            messages.info(request, 'There is no patients asigned to this nurse')
        return render(request, 'medication_nurse/medication_nurse.html', context)
    else:
        return redirect('_404')


# to add medication
def medications(request, med_id):
    if request.user.is_authenticated:
        if request.method == 'POST' and 'btnsave' in request.POST:
            # declare the fields
            med_name = None
            med_frequency = None
            med_amount = None
            med_strength = None
            med_route = None
            med_refills = None
            med_dispense = None
            med_start_date = None
            med_time = None
            med_end_date = None
            comments = None

            # check and get the values from the form 
            if 'med_name' in request.POST:
                med_name = request.POST['med_name']
            else:
                messages.error(request, 'Check in medication name')

            if 'med_frequency' in request.POST:
                med_frequency = request.POST['med_frequency']
            else:
                messages.error(request, 'Check in medication frequency')

            if 'med_amount' in request.POST: 
                med_amount = request.POST['med_amount']
            else: 
                messages.error(request, 'Check in medication amounts')

            if 'med_strength' in request.POST: 
                med_strength = request.POST['med_strength']
            else: 
                messages.error(request, 'Check in medication strength')

            if 'med_route' in request.POST: 
                med_route = request.POST['med_route']
            else: 
                messages.error(request, 'Check in medication route')

            if 'med_refills' in request.POST: 
                med_refills = request.POST['med_refills']
            else: 
                messages.error(request, 'Check in medication refills')

            if 'med_dispense' in request.POST: 
                med_dispense = request.POST['med_dispense']
            else: 
                messages.error(request, 'Check in medication dispense')

            if 'med_start_date' in request.POST: 
                med_start_date = request.POST['med_start_date']
            else: 
                messages.error(request, 'Check medication start date')

            if 'med_end_date' in request.POST: 
                med_end_date = request.POST['med_end_date']
            else: 
                messages.error(request, 'Check medication end date')

            if 'med_time' in request.POST: 
                med_time = request.POST['med_time']
            else: 
                messages.error(request, 'Check medication start time')
            
            if 'comments' in request.POST:
                comments = request.POST['comments']
                comment = Comment(
                        comment=comments,
                        user=request.user,
                        patient=Patient.objects.get(user_id=med_id)
                    )
                comment.save()
                

            if med_name and med_frequency and med_amount and med_strength and \
               med_route and med_refills and med_dispense and med_start_date and \
               med_end_date and med_time:

                patient = Patient.objects.get(user_id=med_id)
                medication = Medication(
                    medication_name=med_name,
                    med_freq=med_frequency,
                    med_amount=med_amount,
                    med_route=med_route,
                    med_refills=med_refills,
                    med_strength=med_strength,
                    med_dispense=med_dispense,
                    med_start_date=med_start_date,
                    med_end_date=med_end_date,
                    med_time=med_time,
                    w_nurse=WorkstationNurse.objects.get(user=request.user),
                    patient=patient,
                    m_nurse=MedicationNurse.objects.get(pk=patient.m_nurse_id)
                )
                medication.save()

                # clear the fields
                med_name = ''
                med_frequency = ''
                med_amount = ''
                med_strength = ''
                med_route = ''
                med_refills = ''
                med_dispense = ''
                med_start_date = ''
                med_time = ''
                med_end_date = ''
                comments = ''

                messages.success(request, 'The medication is added successfully')
            else:
                messages.error(request, 'Please, check the empy fields')
            return render(request,'medication_nurse/medications.html', {
                'med_name': med_name,
                'med_frequency': med_frequency,
                'med_amount': med_amount,
                'med_strength': med_strength,
                'med_route': med_route,
                'med_refills': med_refills,
                'med_dispense': med_dispense,
                'med_start_date': med_start_date,
                'med_time': med_time,
                'med_end_date': med_end_date,
                'comments': comments,
                'is_workstation_nurse': True
                
            })
        elif request.method == 'POST' and 'btnclose' in request.POST:
            return redirect('workstation_nurse')
        else:
            return render(request,'medication_nurse/medications.html')
    else:
        return redirect('_404')
    

# to add vital in offline mode
def vital(request, vital_id):
    if request.user.is_authenticated:
        if request.method == 'POST' and 'btnsave' in request.POST:
            # declare the fields
            heart_rate = None
            spo2 = None
            systolic = None
            diastolic = None
            body_temp = None
            env_temp = None
            vital_time = None
            vital_date = None

            # check and get the values from the form 
            if 'heart_rate' in request.POST:
                heart_rate = request.POST['heart_rate']
            else:
                messages.error(request, 'Check heart rate value')

            if 'spo2' in request.POST:
                spo2 = request.POST['spo2']
            else:
                messages.error(request, 'Check spo2 value')

            if 'systolic' in request.POST: 
                systolic = request.POST['systolic']
            else: 
                messages.error(request, 'Check systolic pressure value')

            if 'diastolic' in request.POST: 
                diastolic = request.POST['diastolic']
            else: 
                messages.error(request, 'Check diastolic pressure value')

            if 'body_temp' in request.POST: 
                body_temp = request.POST['body_temp']
            else: 
                messages.error(request, 'Check body temperature')

            if 'env_temp' in request.POST: 
                env_temp = request.POST['env_temp']
            else: 
                messages.error(request, 'Check environment temperature')

            if 'vital_time' in request.POST: 
                vital_time = request.POST['vital_time']
            else: 
                messages.error(request, 'Check vital time value')

            if 'vital_date' in request.POST: 
                vital_date = request.POST['vital_date']
            else: 
                messages.error(request, 'Check vital date value')

            if heart_rate and spo2 and systolic and diastolic and \
               body_temp and env_temp and vital_date and vital_time:

                patient = Patient.objects.get(user_id=vital_id)
                parameters = PatientParameter(
                    patient=patient,
                    sys_pressure=systolic,
                    dia_pressure = diastolic,
                    HR=heart_rate,
                    spo2=spo2,
                    temp=body_temp,
                    env_temp=env_temp
                    )
                parameters.save()

                # clear the fields
                heart_rate = ''
                spo2 = ''
                systolic = ''
                diastolic = ''
                body_temp = ''
                env_temp = ''
                vital_time = ''
                vital_date = ''

                messages.success(request, 'The vital signs is added successfully')
            else:
                messages.error(request, 'Please, check the empy fields')             
            return render(request, 'medication_nurse/vital.html', {
                'heart_rate': heart_rate,
                'spo2': spo2,
                'systolic': systolic,
                'diastolic': diastolic,
                'body_temp': body_temp,
                'env_temp': env_temp,
                'vital_time': vital_time,
                'vital_date': vital_date,
                'is_workstation_nurse': True
            })

        elif request.method == 'POST' and 'btnclose' in request.POST:
            return redirect('medication_nurse')
        else:
            return render(request,'medication_nurse/vital.html')
    else:
        return redirect('_404')
        

