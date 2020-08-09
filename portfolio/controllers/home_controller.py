from django.http import HttpResponse
from django.shortcuts import render
from websites.models import Website
def home(request):
    websites = Website.objects.all()
    return render(request,'index.html',{'websites':websites})