from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from websites.models import Website
from websites.forms import WebsiteCreationForm

@login_required(login_url="/developpers/login")
def index(request):
    websites = Website.objects.all().filter().order_by("created_at")
    return render(request,'websites/index.html',{'websites':websites})

@login_required(login_url="/developpers/login")
def show(request,slug):
    website = Website.objects.get(slug=slug)
    return render(request,'websites/show.html',{'website':website})

@login_required(login_url="/developpers/login")
def create(request):
    if request.POST:
        form = WebsiteCreationForm(request.POST,request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.developper = request.user
            instance.save()
            return redirect('websites:list')
    form = WebsiteCreationForm()
    return render(request,'websites/create.html',{'form':form});  

@login_required(login_url="/developpers/login")
def edit(request,id):
    website = Website.objects.get(id=id)
    print(website)
    if not website:
        
        return redirect('websites:list')
    if request.POST:
       
       form = WebsiteCreationForm(request.POST,request.FILES,instance=website)
       if form.is_valid():
           form.save()
           return redirect('websites:list')
    
    form = WebsiteCreationForm(instance=website)
    return render(request,'websites/edit.html',{'form':form,'website':website}) 

@login_required(login_url="/developpers/login")
def delete(request,id):
    website=Website.objects.get(id=id)
    if not website:
        website.delete()
        return redirect('websites:list')
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))