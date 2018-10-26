from django.shortcuts import render
from django.core import serializers
import json
from django.http import HttpResponse
from django.conf import settings
from django.core.files.storage import FileSystemStorage

from NLP.models import NLP_MAPS
# Create your views here.
import googlemaps
from . import text2info , audio2text

from .models import NLP_MAPS

def index(converted_text):
    template = 'NLP/index.html'
    print(template)
    map = NLP_MAPS()
    res = {}
    res = text2info.get_info(converted_text)
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
    map.Remarks = res['Remark']
    map.save() 

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
    print("fshuhdsi")
    if request.method == 'POST' and request.FILES['myfile']:
        print("ywuueiwi")
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        converted_text = audio2text.get_text_from_audio(uploaded_file_url)
        index(converted_text)
        # file_path = os.path.join(BASE_DIR, uploaded_file_url)
        # pass_file_path(file_path)
        # index()
        print(uploaded_file_url)
        return render(request, 'NLP/index.html', {
            'uploaded_file_url': uploaded_file_url
        })
    return render(request, 'NLP/upload.html')

    if request.method == 'GET':
        print("jujdsd .....")
        return render(request, 'NLP/upload.html')
