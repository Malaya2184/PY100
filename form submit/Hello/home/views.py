from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages

# from home.models import Contact
# Create your views here.
def index(request):
    # return HttpResponse('this is index page')
    context = {
        'variable': 'Malaya is the boss because Apunich Bhagwaan he vaii bhagwaan he',
        'variable1':'because Apunich Bhagwaan he vaii bhagwaan he'
    }
    return render(request,'index.html',context)


def about(request):
    # return HttpResponse('this is about page')
    return render(request,'about.html')

def services(request):
    # return HttpResponse('this is services page')
    return render(request,'services.html')

def contacts(request):
    # return HttpResponse('this is contacts page')
    if request.method == 'POST' :
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name= name, email= email,phone=phone, desc=desc, date= datetime.today())
        contact.save()
        messages.success(request, 'Message has been send')

    return render(request,'contacts.html')