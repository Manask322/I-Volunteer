from django.http import HttpResponse
from django.shortcuts import render


def audiototext(request):
    #s='HI Hello how are you'
    #return HttpResponse(s)
    return render(request, 'home.html')



def infoextracted(request):
    return HttpResponse('about')
