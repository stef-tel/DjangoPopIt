from django.http import HttpResponse
from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect 
from datetime import datetime
from .forms import SignUpForm
from django.core.mail import send_mail

# Create your views here.
def index(request):    

    # Retourne nombre1, nombre2 et la somme des deux au tpl
    return render(request, 'index.html', locals())

def contact(request):    
    
    #send_mail(
    #    'test from Django popit',
    #    'Here is the message.',
    #    'stef.tellier@gmail.com',
    #    ['stephane.tellier@endexar.com'],
    #    fail_silently=False,
    #)

    # Retourne nombre1, nombre2 et la somme des deux au tpl
    return render(request, 'contact.html', locals())


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            #user = authenticate(username=username, password=raw_password)
            #login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})