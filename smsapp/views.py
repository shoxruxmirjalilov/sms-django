from django.shortcuts import render, redirect
from sendsms.settings import EMAIL_HOST_USER
from . import forms 
from django.core.mail import send_mail
from django.utils import timezone
from smsapp.forms import MyCommentForm
from django.contrib import messages
from twilio.rest import Client


# Create your views here.

def index(request):
    form = forms.Email()
    if request.method == 'POST':
        form = forms.Email(request.POST)
        subject = 'Xabaringiz muvafaqiyatli yuborildi!'
        message = request.POST.get('message')
        email = request.POST.get('email')
        send_mail(subject,
            message, EMAIL_HOST_USER, [email], fail_silently = False)  
        form = MyCommentForm(request.POST)

        account_sid = 'AC6049ea1cda2adee0b79942603c6ba08d'
        auth_token = 'ff0c3308ab303d30a2909455e7bdbb48'
        client = Client(account_sid, auth_token)

        message = client.messages \
                        .create(
                            body="Yangi xabar ma'lumotlar omboriga muvafaqiyatli tarzda saqlandi! Ma'lumotlar omborini tekshiring!",
                            from_='+14438927078',
                            to='+998971401717'
                        )

        if form.is_valid():
            model_instance = form.save(commit=False)
            model_instance.timestamp = timezone.now()
            model_instance.save()
            messages.success(request, 'Xabaringiz muvafaqiyatli yuborildi!')
   
            return redirect('index')
    else:
        form = MyCommentForm()    
    return render(request, 'index.html', {'form':form})
 