from django.shortcuts import redirect, render
from .models import Room, Message
from django.contrib.auth.models import User
from accounts.models import Patient, WorkstationNurse
from django.http import HttpResponse, JsonResponse


# Create your views here.
def chat(request, chat_id):
    if request.user.is_authenticated:
        if Patient.objects.filter(user=request.user).exists():
            # patient
            user = User.objects.get(pk=chat_id)
            patient = Patient.objects.get(user=user)
            room = Room.objects.get(patient=patient)

            return render(request, 'chat/chat.html', {
                'full_name': patient.full_name,
                'username': request.user.username,
                'room': room,
                'is_patient': True,
                'is_nurse': False,
            })
        elif WorkstationNurse.objects.filter(user=request.user).exists():
            # nurse
            user = User.objects.get(pk=chat_id)
            patient = Patient.objects.get(user=user)
            room = Room.objects.get(patient=patient)

            return render(request, 'chat/chat.html', {
                'full_name': patient.w_nurse.full_name,
                'username': request.user.username,
                'room': room,
                'is_patient': False,
                'is_nurse': True,
            })
        else:
            pass  
    else:
        return redirect('_404')


def send(request):
    message = request.POST['message']
    full_name = request.POST['full_name']
    username = request.POST['username']
    room_id = request.POST['room_id']
    
    room = Room.objects.get(pk=room_id)
    user = User.objects.get(username=username)

    new_message = Message.objects.create(value=message, full_name=full_name, user=user, room=room)
    new_message.save()
    # type of user
    if Patient.objects.filter(user=user).exists():
        user_id = user.id
        return JsonResponse({'patient_id': user_id})
    else:
        return HttpResponse('the message has been sent successfully')


def getMessages(request, chat_id):
    room_details = Room.objects.get(pk=chat_id)

    messages = Message.objects.filter(room_id=room_details.id)
    return JsonResponse({"messages":list(messages.values())})