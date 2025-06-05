from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from Home.models import Contact
from django.contrib import messages

# Create your views here.
def index(request):
    context={
        "var":"This is That Blahh"
    }
    
    return render(request,'index.html')

# return HttpResponse("This is HomePage")

def about(request):
    #return HttpResponse("This is AboutPage")
     return render(request,'about.html')

def contact(request):
    #return HttpResponse("this is contact page")
    if request.method =="POST":
        name = request.POST.get('name')
        Email = request.POST.get('Email')
        phone = request.POST.get('phone')
        dcse = request.POST.get('dcse')
        contact=Contact(name=name,Email=Email,phone=phone,dcse=dcse,date=datetime.today())
        contact.save()
        messages.success(request, "Your message has been sent.")
        
    return render(request,'contact.html')




