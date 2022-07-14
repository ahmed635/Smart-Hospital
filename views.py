from django.shortcuts import redirect, render
from .models import Comment
from django.contrib import messages
from accounts.models import Patient, Doctor, WorkstationNurse


# Create your views here.
def comments(request, com_id):
    if request.user.is_authenticated:
        context = None
        if request.method == 'POST' and 'btncomments' in request.POST:        
            if 'comments' in request.POST:
                comments = request.POST['comments']
                patient = Patient.objects.get(user_id=com_id)
                comment = Comment(
                    comment=comments,
                    user=request.user,
                    patient=patient
                )
                comment.save()
                
                if Doctor.objects.filter(user=request.user).exists():
                    context = {
                        'is_doctor': True,
                        'is_workstation_nurse': False,
                        'is_medication_nurse': False
                    }
                elif WorkstationNurse.objects.filter(user=request.user).exists():
                    context = {
                        'is_doctor': False,
                        'is_workstation_nurse': True,
                        'is_medication_nurse': False
                    }
                else:
                    context = {
                        'is_doctor': False,
                        'is_workstation_nurse': False,
                        'is_medication_nurse': True
                    }
                messages.success(request, "Your comments have been saved")
            else:
                messages.error(request, 'Please, enter your comments')
            return render(request, 'comments/comments.html', context)
        elif request.method == 'POST' and 'btnclose' in request.POST:
            if Doctor.objects.filter(user=request.user).exists():
                return redirect('doctor')
            elif WorkstationNurse.objects.filter(user=request.user).exists():
                return redirect('workstation_nurse')
            else:
                # medication nurse
                return redirect('medication_nurse')
        else:
            if Doctor.objects.filter(user=request.user).exists():
                context = {
                    'is_doctor': True,
                    'is_workstation_nurse': False,
                    'is_medication_nurse': False
                }
            elif WorkstationNurse.objects.filter(user=request.user).exists():
                context = {
                    'is_doctor': False,
                    'is_workstation_nurse': True,
                    'is_medication_nurse': False
                }
            else:
                context = {
                    'is_doctor': False,
                    'is_workstation_nurse': False,
                    'is_medication_nurse': True
                }
            return render(request,'comments/comments.html', context)
    else:
        return redirect('_404')
    