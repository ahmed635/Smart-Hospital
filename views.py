from django.shortcuts import render, redirect

# for email validation
import re

# to use the messages import messages from django.contrib
from django.contrib import messages

# to sign up a user
from django.contrib import auth

# get your models
from django.contrib.auth.models import User
from .models import Patient, WorkstationNurse, MedicationNurse, Device, Doctor, Manager, UserInfo
from datetime import date
from medication_nurse.models import Medication
from comments.models import Comment
from chatapp.models import Room

# to redirect a user to admin panel
from django.http import HttpResponseRedirect



def signin(request):
    if request.method == 'POST' and 'btnlogin' in request.POST :
        # variables for the field
        username = None
        password = None
        email = None

        # check if the variable is existed in the request.POST
        if 'email' in request.POST:
            email = request.POST['email']
        else:
            messages.error(request, 'Error in email')
        
        if 'password' in request.POST:
            password = request.POST['password']
        else:
            messages.error(request, 'Error in password')
    
        # check the values from the form
        if email and password:
            # check if email and password are existed in database
            if User.objects.filter(email=email).exists():
                username = User.objects.get(email=email)
                user = auth.authenticate(username=username, password=password)

                # not None means that user is existed in database
                if user is not None:
                    if 'remember_me' not in request.POST:
                        request.session.set_expiry(0)
                    
                    # check type of user
                    if Patient.objects.filter(user_id=user.id).exists():
                        # login 
                        auth.login(request, user)

                        # clear the field
                        email = ''
                        password = ''

                        # check if first login
                        if request.user.last_login is None:
                            return redirect('edit_profile')
                        else:
                            return redirect('patient',request.user.id)
                    elif WorkstationNurse.objects.filter(user_id=user.id).exists():
                        # login 
                        auth.login(request, user)

                        # clear the field
                        email = ''
                        password = ''
                        
                        # check if first login
                        if request.user.last_login is None:
                            return redirect('edit_profile')
                        else:         
                            return redirect('workstation_nurse')
                    elif MedicationNurse.objects.filter(user_id=user.id).exists():
                        # login 
                        auth.login(request, user)
                        
                        # clear the field
                        email = ''
                        password = ''

                        # check if first login
                        if request.user.last_login is None:
                            return redirect('edit_profile')
                        else:
                            return redirect('medication_nurse')
                    elif Doctor.objects.filter(user_id=user.id).exists():
                        # login 
                        auth.login(request, user)

                        # clear the field
                        email = ''
                        password = ''
                        
                        # check if first login
                        if request.user.last_login is None:
                            return redirect('edit_profile')
                        else:
                            return redirect('doctor')
                    elif Manager.objects.filter(user_id=user.id).exists():
                        # login 
                        auth.login(request, user)

                        # clear the field
                        email = ''
                        password = ''

                        # check if first login
                        if request.user.last_login is None:
                            return redirect('edit_profile')
                        else:
                            return redirect('manager')
                    elif User.objects.filter(is_superuser=True).exists():
                        auth.login(request, user)

                        # clear the fields
                        email = ''
                        password = ''

                        # check if first login
                        if request.user.last_login is None:
                            return HttpResponseRedirect('/admin/')
                        else:
                            return HttpResponseRedirect('/admin/')
                    else:
                        return redirect('_404')   
                else:
                    messages.error(request, 'Email or password invalid')
            else:
                messages.error(request, 'Error in email address')
        else:
            messages.error(request, 'Check the empty fields')
        return render(request, 'accounts/signin.html',{
            'password': password,
            'email': email
        })
    else:
        return render(request, 'accounts/signin.html')
        

def logout(request):
    if request.user.is_authenticated:
        auth.logout(request)
    return render(request,'pages/index.html')
    

def signup(request):
    if request.method == 'POST' and 'btnsignup' in request.POST :
        # variables for fields
        username = None
        email = None
        password = None
        confirm_password = None
        user_type = None
        user_added = None

        # after selecting the user_type is patient
        device_id = None
        m_nurse = None
        w_nurse = None

        # to selecting options of device id, workstation and medication nurses
        med_nurses = MedicationNurse.objects.all()
        work_nurses = WorkstationNurse.objects.all()
        device_ids = Device.objects.all()

        # get values from the form
        if 'username' in request.POST:
            username = request.POST['username']
        else:
            messages.error(request, 'Error in username')
        
        if 'email' in request.POST:
            email = request.POST['email']
        else:
            messages.error(request, 'Error in email')
        
        if 'password' in request.POST:
            password = request.POST['password']

        if 'confirm_password' in request.POST:
            confirm_password = request.POST['confirm_password']
        else:
            messages.error(request, 'Error in password')
        
        if 'user_type' in request.POST:
            user_type = request.POST['user_type']
        else:
            messages.error(request, 'Error in user type')
        
        # check the values
        if username and password and email and confirm_password and user_type:
            # check if username is existed and email
            if User.objects.filter(username=username).exists():
                messages.error(request, 'This username is already existed')
            elif User.objects.filter(email=email).exists():
                messages.error(request, 'This email is already existed')
            else:                        
                # check email validations
                pattern = "\w[\w\.-]+@\w[\w\.-]+\.\w+"
                if re.match(pattern, email):
                    # check if passwords are match
                    if password != confirm_password:
                        messages.error(request, 'Passwords did not match ')
                    else:
                        # selecting user type
                        if request.POST['user_type'] == "patient":
                            # get the values from the form
                            if 'device_id' in request.POST:
                                device_id = request.POST['device_id']
                            else:
                                messages.error(request, 'Error in device id')
        
                            if 'm_nurse' in request.POST:
                                m_nurse = request.POST['m_nurse']
                            else:
                                messages.error(request, 'Error in medication nurse')

                            if 'w_nurse' in request.POST:
                                w_nurse = request.POST['w_nurse']
                            else:
                                messages.error(request, 'Error in workstation nurse')
                            
                            # check the values from the form if existed
                            if device_id and w_nurse and m_nurse:
                                # check if the device id is token
                                if Patient.objects.filter(device= device_id).exists():
                                    messages.error(request, 'This device id is already existed')    
                                else:
                                    # CREATE THE USER
                                    user = User.objects.create_user(
                                        username=username, password=password,
                                         email=email
                                    )
                                    user.save()

                                    # ADD USER TO USER INFO MODEL
                                    user_info = UserInfo(user=user)
                                    user_info.save()

                                    # GET DEVICE, MEDICATION NURSE, AND WORKSTATION NURSE
                                    device = Device.objects.get(device_id=device_id)
                                    med_nurse = MedicationNurse.objects.get(full_name=m_nurse)                                            
                                    work_nurse = WorkstationNurse.objects.get(full_name=w_nurse)
                                    
                                    # add a patient 
                                    patient = Patient(
                                        user = user,
                                        device=device,
                                        w_nurse=work_nurse,
                                        m_nurse=med_nurse,
                                        user_info=user_info
                                    )
                                    patient.save()

                                    # add to room
                                    room = Room.objects.create(patient=patient)
                                    room.save()

                                    # clear the fiels
                                    username = ''
                                    password = ''
                                    confirm_password = ''
                                    user_type = ''
                                    email = ''
                                    w_nurse = ''
                                    m_nurse = ''
                                    device_id = ''

                                    # success message
                                    messages.success(request, 'Your account is created')
                                    user_added = True
                            else:
                                messages.error(request , 'Error in device id or medication nurse or workstation nurse')        
                        elif request.POST["user_type"] == "workstation_nurse":
                            user = User.objects.create_user(username=username, password=password, email=email)
                            user.save()
                            user_info = UserInfo(user=user)
                            user_info.save()

                            # create a workstation nurse
                            workstation_nurse = WorkstationNurse(user=user)
                            workstation_nurse.save()

                            # clear the fiels
                            username = ''
                            password = ''
                            confirm_password = ''
                            user_type = ''
                            email = ''

                            # success message
                            messages.success(request, 'Your account is created')
                            user_added = True
                        elif request.POST["user_type"] == "medication_nurse":
                            user = User.objects.create_user(username=username, password=password, email=email)
                            user.save()
                            user_info = UserInfo(user=user)
                            user_info.save()
                            medication_nurse = MedicationNurse(user=user)
                            medication_nurse.save()

                            # clear the fiels
                            username = ''
                            password = ''
                            confirm_password = ''
                            user_type = ''
                            email = ''

                            # success message
                            messages.success(request, 'Your account is created')
                            user_added = True
                        elif request.POST["user_type"] == "manager":
                            # set this user as superuser to get all the permission of the system
                            user = User.objects.create_user(username=username, password=password, email=email, is_staff=True, is_superuser=True)
                            user.save()
                            user_info = UserInfo(user=user)
                            user_info.save()
                            manager = Manager(user=user)
                            manager.save()

                            # clear the fiels
                            username = ''
                            password = ''
                            confirm_password = ''
                            user_type = ''
                            email = ''

                            # success message
                            messages.success(request, 'Your account is created')
                            user_added = True   
                        elif request.POST["user_type"] == "doctor":
                            user = User.objects.create_user(username=username, password=password, email=email)
                            user.save()
                            user_info = UserInfo(user=user)
                            user_info.save()
                            doctor = Doctor(user=user)
                            doctor.save()

                            # clear the fiels
                            username = ''
                            password = ''
                            confirm_password = ''
                            user_type = ''
                            email = ''

                            # success message
                            messages.success(request, 'Your account is created')
                            user_added = True 
                        else:
                            messages.error(request, "Please, select a user type")     
                else:
                    messages.error(request, 'Invalid email')
        else:
            messages.error(request, 'check empty fields')
        return render(request, 'accounts/signup.html', {
            'username': username,
            'email': email,
            'password': password,
            'confirm_password': confirm_password,
            'user_type': user_type,
            'device_id': device_id,
            'm_nurse': m_nurse,
            'w_nurse': w_nurse,
            'med_nurses': med_nurses,
            'work_nurses': work_nurses,
            'device_ids': device_ids,
            'user_add': user_added
        })
    else:
        return render(request, 'accounts/signup.html',{
            'med_nurses': MedicationNurse.objects.all(),
            'work_nurses': WorkstationNurse.objects.all(),
            'device_ids': Device.objects.all(),
        })
    

def profile(request, pat_id):
    if request.user.is_authenticated:
        # varibles for fields
        context = None
        user_info = None
        email = None
        user_type = None
        medication = None
        no_medication = True
        workstation_nurse_comments = None
        doctor_comments = None
        medication_nurse_comments = None
        no_comments = True

        # check if a user want to see patient profile or not
        if request.user.id == pat_id:
            # check type of user
            if Patient.objects.filter(user_id=pat_id).exists():
                user_type = Patient.objects.get(user=request.user)
                user_info = UserInfo.objects.get(user=request.user)
                email = request.user.email
                
                if user_info.birth_date is not None: 
                    date_today = date.today()
                    age = date_today.year - user_info.birth_date.year - ((date_today.month, date_today.day) < (user_info.birth_date.month, user_info.birth_date.day))
                else:
                    age = 'undetermined'

                # get the patient's medicine
                medication = Medication.objects.filter(patient=user_type)
                if Medication.objects.filter(patient=user_type).exists():
                    no_medication = False

                # get the comments of the patient
                if Comment.objects.filter(patient=user_type).exists():
                    no_comments = False
                    workstation_nurse_comments = Comment.objects.filter(patient=user_type,user=user_type.w_nurse.user_id)                
                    medication_nurse_comments = Comment.objects.filter(patient=user_type, user=user_type.m_nurse.user_id)
                    doc = Comment.objects.filter(patient=user_type)
                    doc2 = doc.exclude(user=user_type.m_nurse.user_id)
                    doctor_comments = doc2.exclude(user=user_type.w_nurse.user_id)
                context = {
                    'user_type': user_type,
                    'user_info': user_info,
                    'email': email,
                    'medication': medication,
                    'age': age,
                    'is_patient': True,
                    'is_doctor': False,
                    'is_medication_nurse': False,
                    'is_workstation_nurse': False,
                    'is_manager': False,
                    'no_medication': no_medication,               
                }
            elif WorkstationNurse.objects.filter(user_id=pat_id).exists():
                user_info = UserInfo.objects.get(user=request.user)
                email = request.user.email
                
                if user_info.birth_date is not None:   
                    date_today = date.today()
                    age = date_today.year - user_info.birth_date.year - ((date_today.month, date_today.day) < (user_info.birth_date.month, user_info.birth_date.day))
                else:
                    age = 'undetermined'

                context = {
                    'user_type': WorkstationNurse.objects.get(user=request.user),
                    'user_info': user_info,
                    'email': email,
                    'age': age,
                    'is_patient': False,
                    'is_doctor': False,
                    'is_medication_nurse': False,
                    'is_workstation_nurse': True,
                    'is_manager': False,               
                }
            elif MedicationNurse.objects.filter(user_id=pat_id).exists():
                user_info = UserInfo.objects.get(user=request.user)
                email = request.user.email
                
                if user_info.birth_date is not None: 
                    date_today = date.today()
                    age = date_today.year - user_info.birth_date.year - ((date_today.month, date_today.day) < (user_info.birth_date.month, user_info.birth_date.day))
                else:
                    age = 'undetermined'
                
                context = {
                    'user_type': MedicationNurse.objects.get(user=request.user),
                    'user_info': user_info,
                    'email': email,
                    'age': age,
                    'is_patient': False,
                    'is_doctor': False,
                    'is_medication_nurse': True,
                    'is_workstation_nurse': False,
                    'is_manager': False,               
                }
            elif Doctor.objects.filter(user_id=pat_id).exists():
                user_info = UserInfo.objects.get(user=request.user)
                email = request.user.email
                if user_info.birth_date is not None:     
                    date_today = date.today()
                    age = date_today.year - user_info.birth_date.year - ((date_today.month, date_today.day) < (user_info.birth_date.month, user_info.birth_date.day))
                else:
                    age = 'undetermined'

                context = {
                    'user_type': Doctor.objects.get(user=request.user),
                    'user_info': user_info,
                    'email': email,
                    'age': age,
                    'is_patient': False,
                    'is_doctor': True,
                    'is_medication_nurse': False,
                    'is_workstation_nurse': False,
                    'is_manager': False,               
                }
            elif Manager.objects.filter(user_id=pat_id).exists():
                email = request.user.email
                
                user_info = UserInfo.objects.get(user=request.user)
                if user_info.birth_date is not None: 
                    date_today = date.today()
                    age = date_today.year - user_info.birth_date.year - ((date_today.month, date_today.day) < (user_info.birth_date.month, user_info.birth_date.day))
                else:
                    age = 'undetermined'

                context = {
                    'user_type': Manager.objects.get(user=request.user),
                    'user_info': user_info,
                    'email': email,
                    'age': age,
                    'is_patient': False,
                    'is_doctor': False,
                    'is_medication_nurse': False,
                    'is_workstation_nurse': False,
                    'is_manager': True,               
                }
            else:
                pass
            return render(request, 'accounts/profile.html', context)
        else:
            # a user wants to see patient profile
            user_type = Patient.objects.get(user_id=pat_id) # user_type = patient
            user_info = UserInfo.objects.get(user_id=pat_id)
            user = User.objects.get(pk=pat_id)
            email = user.email

            # get the medicine
            medication = Medication.objects.filter(patient=user_type)
            if Medication.objects.filter(patient=user_type).exists():
                no_medication = False
         
            # get the comments of the patient
            if Comment.objects.filter(patient=user_type).exists():
                no_comments = False
                workstation_nurse_comments = Comment.objects.filter(patient=user_type,user=user_type.w_nurse.user_id)                
                medication_nurse_comments = Comment.objects.filter(patient=user_type, user=user_type.m_nurse.user_id)

                doc = Comment.objects.filter(patient=user_type)
                doc2 = doc.exclude(user=user_type.m_nurse.user_id)
                doctor_comments = doc2.exclude(user=user_type.w_nurse.user_id)


            # check if birth date is not none
            if user_info.birth_date is not None:   
                date_today = date.today()
                age = date_today.year - user_info.birth_date.year - ((date_today.month, date_today.day) < (user_info.birth_date.month, user_info.birth_date.day))
            else:
                age = 'undetermined'

            # check type of user
            if WorkstationNurse.objects.filter(user=request.user):
                context = {
                    'user_type': user_type,
                    'user_info': user_info,
                    'email': email,
                    'medication': medication,
                    'age': age,
                    'is_patient': True,
                    'is_workstation_nurse': False,
                    'is_medication_nurse': False,
                    'is_doctor': False,
                    'is_manager': False,
                    'user_is_workstation_nurse': True,
                    'user_is_doctor': False,
                    'user_is_medication_nurse': False,
                    'no_medication': no_medication,
                    'no_comments': no_comments,
                    'workstation_nurse_comments': workstation_nurse_comments,
                    'medication_nurse_comments': medication_nurse_comments,
                    'doctor_comments': doctor_comments,
                }
            elif Doctor.objects.filter(user=request.user):
                context = {
                    'user_type': user_type,
                    'user_info': user_info,
                    'email': email,
                    'medication': medication,
                    'age': age,
                    'is_patient': True,
                    'is_workstation_nurse': False,
                    'is_medication_nurse': False,
                    'is_doctor': True,
                    'is_manager': False,
                    'user_is_workstation_nurse': False,
                    'user_is_doctor': True,
                    'user_is_medication_nurse': False,
                    'no_medication': no_medication,
                    'no_comments': no_comments,
                    'workstation_nurse_comments': workstation_nurse_comments,
                    'medication_nurse_comments': medication_nurse_comments,
                    'doctor_comments': doctor_comments,
                }
            else:
                context = {
                    'user_type': user_type,
                    'user_info': user_info,
                    'email': email,
                    'medication': medication,
                    'age': age,
                    'is_patient': True,
                    'is_workstation_nurse': False,
                    'is_medication_nurse': True,
                    'is_doctor': False,
                    'is_manager': False,
                    'user_is_workstation_nurse': False,
                    'user_is_doctor': False,
                    'user_is_medication_nurse': True,
                    'no_medication': no_medication,
                    'no_comments': no_comments,
                    'workstation_nurse_comments': workstation_nurse_comments,
                    'medication_nurse_comments': medication_nurse_comments,
                    'doctor_comments': doctor_comments,
                }
        return render (request, 'accounts/profile.html', context)
    else:
        return redirect('_404')
    

def edit_profile(request):
    if request.user.is_authenticated:
        # check type of user (patient, doctor, workstation nurse, medication nurse, manager, admin, others)
        if Patient.objects.filter(user=request.user).exists():
            if request.method == 'POST' and 'btnsave' in request.POST:
                patient = Patient.objects.get(user=request.user)
                user_info = UserInfo.objects.get(user=request.user)

                # check the values
                if  request.POST['full_name'] and request.POST['email'] and \
                    request.POST['address_1'] and request.POST['address_2'] and\
                    request.POST['country'] and request.POST['city'] and \
                    request.POST['state'] and request.POST['zipcode'] and \
                    request.POST['birth_date'] and request.POST['gender'] and \
                    request.POST['number_1'] and request.POST['number_2']:
                    
                    # get the values from the request and asign it to patient
                    patient.full_name = request.POST['full_name']
                    patient.has_insurance = request.POST['has_insured']
                    patient.has_covid = request.POST['has_covid']
                    patient.has_hypertension = request.POST['has_hypertension']
                    patient.has_diabetes = request.POST['has_diabetes']
                    patient.insurance_company = request.POST['insurance_company']
                    user_info.address_1 = request.POST['address_1']
                    user_info.address_2 = request.POST['address_2']
                    user_info.country = request.POST['country']
                    user_info.city = request.POST['city']
                    user_info.state = request.POST['state']
                    user_info.zip_code = request.POST['zipcode']
                    user_info.phone_number_1 = request.POST['number_1']
                    user_info.phone_number_2 = request.POST['number_2']
                    user_info.gender = request.POST['gender']
                    user_info.birth_date = request.POST['birth_date']
                    patient.save()
                    user_info.save()
                    messages.success(request, 'Your changes has been saved')
                    # return render(request, 'accounts/edit_profile.html')
                    
                else:
                    messages.error(request, 'Check your empty fields')
                return redirect('edit_profile')
            elif request.method == 'POST' and 'btnchange_password' in request.POST:
                # check the values
                if request.POST['confirm_password'] and request.POST['password']:
                    # check if passwords are match
                    if request.POST['password'] != request.POST['confirm_password']:
                        messages.error(request, 'Passwords did not match ')
                    else:
                        # set the new password
                        request.user.set_password(request.POST['password'])
                        request.user.save()
                        auth.login(request,request.user)
                        messages.success(request, 'Your password has been chanaged')    
                else:
                    messages.error(request, 'Check your empty fields')
                return redirect('edit_profile')
            else:
                # check is the user is exits
                if request.user is not None and request.user.id != None:
                    patient = Patient.objects.get(user=request.user)
                    user_info = UserInfo.objects.get(user=request.user)
                    context = {
                        'current_password': request.user.password,
                        'email': request.user.email,
                        'full_name': patient.full_name,
                        'has_covid': patient.has_covid,
                        'has_insured': patient.has_insurance,
                        'has_hypertension': patient.has_hypertension,
                        'has_diabetes': patient.has_diabetes,
                        'insurance_company': patient.insurance_company,
                        'gender': user_info.gender,
                        'birth_date': user_info.birth_date,
                        'number_1': user_info.phone_number_1,
                        'number_2': user_info.phone_number_2,
                        'country': user_info.country,
                        'city': user_info.city,
                        'state': user_info.state,
                        'address_1': user_info.address_1,
                        'address_2': user_info.address_2,
                        'zipcode': user_info.zip_code,
                        'is_patient': True,
                        'is_workstation_nurse': False,
                        'is_medication_nurse': False,
                        'is_manager': False,
                        'is_doctor': False, 
                    }
                    return render(request , 'accounts/edit_profile.html' , context)
                else:
                    return redirect('_404')
        elif WorkstationNurse.objects.filter(user=request.user).exists():
            if request.method == 'POST' and 'btnsave' in request.POST:
                workstation_nurse = WorkstationNurse.objects.get(user=request.user)
                user_info = UserInfo.objects.get(user=request.user)

                # check the values
                if  request.POST['full_name'] and request.POST['email'] and \
                    request.POST['address_1'] and request.POST['address_2'] and\
                    request.POST['country'] and request.POST['city'] and \
                    request.POST['state'] and request.POST['zipcode'] and \
                    request.POST['birth_date'] and request.POST['gender'] and \
                    request.POST['number_1'] and request.POST['number_2']:
                    
                    # get the values from the request and asign it to patient
                    workstation_nurse.full_name = request.POST['full_name']
                    user_info.address_1 = request.POST['address_1']
                    user_info.address_2 = request.POST['address_2']
                    user_info.country = request.POST['country']
                    user_info.city = request.POST['city']
                    user_info.state = request.POST['state']
                    user_info.zip_code = request.POST['zipcode']
                    user_info.phone_number_1 = request.POST['number_1']
                    user_info.phone_number_2 = request.POST['number_2']
                    user_info.gender = request.POST['gender']
                    user_info.birth_date = request.POST['birth_date']
                    workstation_nurse.save()
                    user_info.save()
                    messages.success(request, 'Your changes has been saved')
                    # return render(request, 'accounts/edit_profile.html')
                    
                else:
                    messages.error(request, 'Check your empty fields')
                return redirect('edit_profile')
            elif request.method == 'POST' and 'btnchange_password' in request.POST:
                # check the values
                if request.POST['confirm_password'] and request.POST['password']:
                    # check if passwords are match
                    if request.POST['password'] != request.POST['confirm_password']:
                        messages.error(request, 'Passwords did not match ')
                    else:
                        # set the new password
                        request.user.set_password(request.POST['password'])
                        request.user.save()
                        auth.login(request,request.user)
                        messages.success(request, 'Your password has been chanaged')    
                else:
                    messages.error(request, 'Check your empty fields')
                return redirect('edit_profile')
            else:
                # check is the user is exits
                if request.user is not None and request.user.id != None:
                    workstation_nurse = WorkstationNurse.objects.get(user=request.user)
                    user_info = UserInfo.objects.get(user=request.user)
                    context = {
                        'current_password': request.user.password,
                        'email': request.user.email,
                        'full_name': workstation_nurse.full_name,
                        'gender': user_info.gender,
                        'birth_date': user_info.birth_date,
                        'number_1': user_info.phone_number_1,
                        'number_2': user_info.phone_number_2,
                        'country': user_info.country,
                        'city': user_info.city,
                        'state': user_info.state,
                        'address_1': user_info.address_1,
                        'address_2': user_info.address_2,
                        'zipcode': user_info.zip_code,
                        'is_patient': False,
                        'is_workstation_nurse': True,
                        'is_medication_nurse': False,
                        'is_manager': False,
                        'is_doctor': False, 
                    }
                    return render(request , 'accounts/edit_profile.html' , context)
                else:
                    return redirect('_404')
        elif MedicationNurse.objects.filter(user=request.user).exists():
            if request.method == 'POST' and 'btnsave' in request.POST:
                medication_nurse = MedicationNurse.objects.get(user=request.user)
                user_info = UserInfo.objects.get(user=request.user)

                # check the values
                if  request.POST['full_name'] and request.POST['email'] and \
                    request.POST['address_1'] and request.POST['address_2'] and\
                    request.POST['country'] and request.POST['city'] and \
                    request.POST['state'] and request.POST['zipcode'] and \
                    request.POST['birth_date'] and request.POST['gender'] and \
                    request.POST['number_1'] and request.POST['number_2']:
                    
                    # get the values from the request and asign it to patient
                    medication_nurse.full_name = request.POST['full_name']
                    user_info.address_1 = request.POST['address_1']
                    user_info.address_2 = request.POST['address_2']
                    user_info.country = request.POST['country']
                    user_info.city = request.POST['city']
                    user_info.state = request.POST['state']
                    user_info.zip_code = request.POST['zipcode']
                    user_info.phone_number_1 = request.POST['number_1']
                    user_info.phone_number_2 = request.POST['number_2']
                    user_info.gender = request.POST['gender']
                    user_info.birth_date = request.POST['birth_date']
                    medication_nurse.save()
                    user_info.save()
                    messages.success(request, 'Your changes has been saved')
                    # return render(request, 'accounts/edit_profile.html')
                    
                else:
                    messages.error(request, 'Check your empty fields')
                return redirect('edit_profile')
            elif request.method == 'POST' and 'btnchange_password' in request.POST:
                # check the values
                if request.POST['confirm_password'] and request.POST['password']:
                    # check if passwords are match
                    if request.POST['password'] != request.POST['confirm_password']:
                        messages.error(request, 'Passwords did not match ')
                    else:
                        # set the new password
                        request.user.set_password(request.POST['password'])
                        request.user.save()
                        auth.login(request,request.user)
                        messages.success(request, 'Your password has been chanaged')    
                else:
                    messages.error(request, 'Check your empty fields')
                return redirect('edit_profile')
            else:
                # check is the user is exits
                if request.user is not None and request.user.id != None:
                    medication_nurse = MedicationNurse.objects.get(user=request.user)
                    user_info = UserInfo.objects.get(user=request.user)
                    context = {
                        'current_password': request.user.password,
                        'email': request.user.email,
                        'full_name': medication_nurse.full_name,
                        'gender': user_info.gender,
                        'birth_date': user_info.birth_date,
                        'number_1': user_info.phone_number_1,
                        'number_2': user_info.phone_number_2,
                        'country': user_info.country,
                        'city': user_info.city,
                        'state': user_info.state,
                        'address_1': user_info.address_1,
                        'address_2': user_info.address_2,
                        'zipcode': user_info.zip_code,
                        'is_patient': False,
                        'is_workstation_nurse': False,
                        'is_medication_nurse': True,
                        'is_manager': False,
                        'is_doctor': False,

                    }
                    return render(request , 'accounts/edit_profile.html' , context)
                else:
                    return redirect('_404')
        elif Doctor.objects.filter(user=request.user).exists():
            if request.method == 'POST' and 'btnsave' in request.POST:
                doctor = Doctor.objects.get(user=request.user)
                user_info = UserInfo.objects.get(user=request.user)

                # check the values
                if  request.POST['full_name'] and request.POST['email'] and \
                    request.POST['address_1'] and request.POST['address_2'] and\
                    request.POST['country'] and request.POST['city'] and \
                    request.POST['state'] and request.POST['zipcode'] and \
                    request.POST['birth_date'] and request.POST['gender'] and \
                    request.POST['number_1'] and request.POST['number_2']:
                    
                    # get the values from the request and asign it to patient
                    doctor.full_name = request.POST['full_name']
                    user_info.address_1 = request.POST['address_1']
                    user_info.address_2 = request.POST['address_2']
                    user_info.country = request.POST['country']
                    user_info.city = request.POST['city']
                    user_info.state = request.POST['state']
                    user_info.zip_code = request.POST['zipcode']
                    user_info.phone_number_1 = request.POST['number_1']
                    user_info.phone_number_2 = request.POST['number_2']
                    user_info.gender = request.POST['gender']
                    user_info.birth_date = request.POST['birth_date']
                    doctor.save()
                    user_info.save()
                    messages.success(request, 'Your changes has been saved')
                    # return render(request, 'accounts/edit_profile.html')
                    
                else:
                    messages.error(request, 'Check your empty fields')
                return redirect('edit_profile')
            elif request.method == 'POST' and 'btnchange_password' in request.POST:
                # check the values
                if request.POST['confirm_password'] and request.POST['password']:
                    # check if passwords are match
                    if request.POST['password'] != request.POST['confirm_password']:
                        messages.error(request, 'Passwords did not match ')
                    else:
                        # set the new password
                        request.user.set_password(request.POST['password'])
                        request.user.save()
                        auth.login(request,request.user)
                        messages.success(request, 'Your password has been chanaged')    
                else:
                    messages.error(request, 'Check your empty fields')
                return redirect('edit_profile')
            else:
                # check is the user is exits
                if request.user is not None and request.user.id != None:
                    doctor = Doctor.objects.get(user=request.user)
                    user_info = UserInfo.objects.get(user=request.user)
                    context = {
                        'current_password': request.user.password,
                        'email': request.user.email,
                        'full_name': doctor.full_name,
                        'gender': user_info.gender,
                        'birth_date': user_info.birth_date,
                        'number_1': user_info.phone_number_1,
                        'number_2': user_info.phone_number_2,
                        'country': user_info.country,
                        'city': user_info.city,
                        'state': user_info.state,
                        'address_1': user_info.address_1,
                        'address_2': user_info.address_2,
                        'zipcode': user_info.zip_code,
                        'is_patient': False,
                        'is_workstation_nurse': False,
                        'is_medication_nurse': False,
                        'is_manager': False,
                        'is_doctor': True, 
                    }
                    return render(request , 'accounts/edit_profile.html' , context)
                else:
                    return redirect('_404')
        elif Manager.objects.filter(user=request.user).exists():
            if request.method == 'POST' and 'btnsave' in request.POST:
                manager = Manager.objects.get(user=request.user)
                user_info = UserInfo.objects.get(user=request.user)

                # check the values
                if  request.POST['full_name'] and request.POST['email'] and \
                    request.POST['address_1'] and request.POST['address_2'] and\
                    request.POST['country'] and request.POST['city'] and \
                    request.POST['state'] and request.POST['zipcode'] and \
                    request.POST['birth_date'] and request.POST['gender'] and \
                    request.POST['number_1'] and request.POST['number_2']:
                    
                    # get the values from the request and asign it to patient
                    manager.full_name = request.POST['full_name']
                    user_info.address_1 = request.POST['address_1']
                    user_info.address_2 = request.POST['address_2']
                    user_info.country = request.POST['country']
                    user_info.city = request.POST['city']
                    user_info.state = request.POST['state']
                    user_info.zip_code = request.POST['zipcode']
                    user_info.phone_number_1 = request.POST['number_1']
                    user_info.phone_number_2 = request.POST['number_2']
                    user_info.gender = request.POST['gender']
                    user_info.birth_date = request.POST['birth_date']
                    manager.save()
                    user_info.save()
                    messages.success(request, 'Your changes has been saved')
                    # return render(request, 'accounts/edit_profile.html')
                    
                else:
                    messages.error(request, 'Check your empty fields')
                return redirect('edit_profile')
            elif request.method == 'POST' and 'btnchange_password' in request.POST:
                # check the values
                if request.POST['confirm_password'] and request.POST['password']:
                    # check if passwords are match
                    if request.POST['password'] != request.POST['confirm_password']:
                        messages.error(request, 'Passwords did not match ')
                    else:
                        # set the new password
                        request.user.set_password(request.POST['password'])
                        request.user.save()
                        auth.login(request,request.user)
                        messages.success(request, 'Your password has been chanaged')    
                else:
                    messages.error(request, 'Check your empty fields')
                return redirect('edit_profile')
            else:
                # check is the user is exits
                if request.user is not None and request.user.id != None:
                    manager = Manager.objects.get(user=request.user)
                    user_info = UserInfo.objects.get(user=request.user)
                    context = {
                        'current_password': request.user.password,
                        'email': request.user.email,
                        'full_name': manager.full_name,
                        'gender': user_info.gender,
                        'birth_date': user_info.birth_date,
                        'number_1': user_info.phone_number_1,
                        'number_2': user_info.phone_number_2,
                        'country': user_info.country,
                        'city': user_info.city,
                        'state': user_info.state,
                        'address_1': user_info.address_1,
                        'address_2': user_info.address_2,
                        'zipcode': user_info.zip_code,
                        'is_patient': False,
                        'is_workstation_nurse': False,
                        'is_medication_nurse': False,
                        'is_manager': True,
                        'is_doctor': False,
                    }
                    return render(request , 'accounts/edit_profile.html' , context)
                else:
                    return redirect('_404')
        elif User.objects.filter(is_superuser=request.user.is_superuser).exists():
            if request.method == 'POST' and 'btnsave' in request.POST:
                user_info = UserInfo.objects.get(user=request.user)

                # check the values
                if  request.POST['full_name'] and request.POST['email'] and \
                    request.POST['address_1'] and request.POST['address_2'] and\
                    request.POST['country'] and request.POST['city'] and \
                    request.POST['state'] and request.POST['zipcode'] and \
                    request.POST['birth_date'] and request.POST['gender'] and \
                    request.POST['number_1'] and request.POST['number_2']:
                    
                    # get the values from the request and asign it to patient
                    request.user.username = request.POST['full_name']
                    user_info.address_1 = request.POST['address_1']
                    user_info.address_2 = request.POST['address_2']
                    user_info.country = request.POST['country']
                    user_info.city = request.POST['city']
                    user_info.state = request.POST['state']
                    user_info.zip_code = request.POST['zipcode']
                    user_info.phone_number_1 = request.POST['number_1']
                    user_info.phone_number_2 = request.POST['number_2']
                    user_info.gender = request.POST['gender']
                    user_info.birth_date = request.POST['birth_date']
                    user_info.save()
                    messages.success(request, 'Your changes has been saved')  
                else:
                    messages.error(request, 'Check your empty fields')
                return redirect('edit_profile')
            elif request.method == 'POST' and 'btnchange_password' in request.POST:
                # check the values
                if request.POST['confirm_password'] and request.POST['password']:
                    # check if passwords are match
                    if request.POST['password'] != request.POST['confirm_password']:
                        messages.error(request, 'Passwords did not match ')
                    else:
                        # set the new password
                        request.user.set_password(request.POST['password'])
                        request.user.save()
                        auth.login(request,request.user)
                        messages.success(request, 'Your password has been chanaged')    
                else:
                    messages.error(request, 'Check your empty fields')
                return redirect('edit_profile')
            else:
                # check is the user is exits
                if request.user is not None and request.user.id != None:
                    user_info = UserInfo.objects.get(user=request.user)
                    context = {
                        'current_password': request.user.password,
                        'email': request.user.email,
                        'full_name': request.user.username,
                        'gender': user_info.gender,
                        'birth_date': user_info.birth_date,
                        'number_1': user_info.phone_number_1,
                        'number_2': user_info.phone_number_2,
                        'country': user_info.country,
                        'city': user_info.city,
                        'state': user_info.state,
                        'address_1': user_info.address_1,
                        'address_2': user_info.address_2,
                        'zipcode': user_info.zip_code,
                        'is_patient': False,
                        'is_workstation_nurse': False,
                        'is_medication_nurse': False,
                        'is_manager': False,
                        'is_doctor': False, 
                    }
                    return render(request , 'accounts/edit_profile.html' , context)
                else:
                    return redirect('_404')
        else:
            return redirect('_404')
    else:
        return redirect('signin')
    

def reset_password(request):
    if request.method == 'POST' and 'btnresetpassword' in request.POST:
        password = None
        confirm_password = None

        # get the email from django session
        email = request.session.get('email')
    
        # get the user 
        user = User.objects.get(email=email)

        # login to avoid anomanous user 
        auth.login(request, user)

        if 'password' in request.POST:
            password = request.POST['password']

        if 'confirm_password' in request.POST:
            confirm_password = request.POST['confirm_password']
        else:
            messages.error(request, 'Error in password')
        
        if password and confirm_password:
            # change the password
            # check if passwords are match
            if request.POST['password'] != request.POST['confirm_password']:
                messages.error(request, 'Passwords did not match ')
                return render(request, 'accounts/reset_password.html', {
                    'password': password,
                    'confirm_password': confirm_password,
                })
            else:
                # set the new password
                request.user.set_password(request.POST['password'])
                user.save()
                messages.success(request, 'Your password has been reset')
                return redirect('signin')
        else:
            messages.err(request, 'Error in password and empty password')
            return render(request, 'accounts/reset_password.html', {
                'password': password,
                'confirm_password': confirm_password,
            })    
    else:
        return render(request, 'accounts/reset_password.html')
    
    
def forget_password(request):
    if request.user.is_authenticated:
        return redirect('_404')
    else:
        if request.method == 'POST' and 'btnresetpassword' in request.POST:
            email = None

            if 'email' in request.POST:
                email = request.POST['email']
            else:
                messages.err(request, 'Enter your email address')

            if email:
                if User.objects.filter(email=email).exists():
                    # sending the email address useing django session
                    request.session['email'] = email
                    return redirect('reset_password')
                else:
                    messages.error(request, 'This email address does not exist')
                    return render(request, 'accounts/forget_password.html',{'email':email})
            else:
               messages.error(request, 'Enter your email address')
               return render(request, 'accounts/forget_password.html') 
        else:
            # the user want to see forget password page
            return render(request, 'accounts/forget_password.html')
