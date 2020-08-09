from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth import login,authenticate,logout
from developpers.forms import DevelopperFormRegister,DevelopperFormLogin

def index(request):
    return render(request,'developpers/index.html')

def register(request):
    if(request.user.is_authenticated):
        return redirect('home')
    if request.method=='POST':
        form = DevelopperFormRegister(request.POST,request.FILES)
        if form.is_valid():
            user=form.save()
            login(request,user)
            return redirect('home')
        return render(request,'developpers/register.html',{'form':form})
    else:
        form = DevelopperFormRegister()
    return render(request,'developpers/register.html',{'form':form})

def login_(request):
    if(request.user.is_authenticated):
        return redirect('home')
    if request.POST:
        form = DevelopperFormLogin(request.POST)
        if form.is_valid():
            user = authenticate(email =request.POST['email'],password=request.POST['password'])
            if user:
                login(request,user)
                if request.POST.get('next',0)!=0:
                    return redirect(request.POST['next'])
                return redirect('home')
        return render(request,'developpers/login.html',{'form':form})
    else:
        form=DevelopperFormLogin()
        return render(request,'developpers/login.html',{'form':form})

def logout_(request):
    logout(request)
    return redirect('home')
    