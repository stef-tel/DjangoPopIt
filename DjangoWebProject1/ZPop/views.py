from django.http import HttpResponse
from django.http import Http404
from django.shortcuts import render, get_list_or_404, redirect 
from datetime import datetime
from ZPop.models import Zlogin

# Create your views here.
def main(request):    

    # Retourne nombre1, nombre2 et la somme des deux au tpl
    return render(request, 'main.html', locals())




def zlogin(request):    

    # Return list of existing zlogin or 404 if none found
    zloginList = get_list_or_404(Zlogin)
    return render(request, 'zlogin.html', locals())



def zloginNew(request):    

    return render(request, 'zloginNew.html', locals())