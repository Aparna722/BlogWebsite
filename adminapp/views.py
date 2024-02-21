from django.shortcuts import render
from django.http import HttpResponse
from userapp.models import *
from adminapp.models import *
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError

# Create your views here.
def index1(request):
    return render(request,"indext1.html")

def indexad(request):
    return render(request,"indexad.html")

def checkad(request):
    blogdetails=Blog.objects.all()
    context={
        'blogdetails':blogdetails
    }
    return render(request,"checkad.html",context)