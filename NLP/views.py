from django.shortcuts import render
from django.core import serializers
import json
from django.http import HttpResponse

from NLP.models import NLP_MAPS
# Create your views here.
import googlemaps
from . import text2info

from .models import NLP_MAPS

def index(request):
    template = 'NLP/index.html'
    map = NLP_MAPS()
    res = {}
    res = text2info.get_info()
    print("here ", res)
    gmaps = googlemaps.Client(key='AIzaSyBdl9Xvi8Yipfx-ldaB9RtluwGEyuU1KHM')
    print("kiops")
    geocode_result = gmaps.geocode(res['Address'])
    print("asaasa")
    print(geocode_result)
    # print(geocode_result)
    map.Address = res['Address']
    map.x = geocode_result[0]['geometry']['location']['lat']
    map.y = geocode_result[0]['geometry']['location']['lng']
    map.intensity = res['Intensity']
    map.save()
    return render(request,template,{'res':res})  

def dashboard(request):
    address = NLP_MAPS.objects.all()
    return render(request,'dashboard.html',{'address': address})

def home(request):
    return render(request,'Home/home.html') 

def maps(request):
    address = NLP_MAPS.objects.values('id','x','y','Address')
    # serial = serializers.serialize('json', [ address, ])
    json_data = json.dumps(list(address))
    return render(request,'NLP/maps.html',{'address':json_data})

def upload(request):
    return render(request,'NLP/upload.html') 
    