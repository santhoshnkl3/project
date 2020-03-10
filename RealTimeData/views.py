from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import LiveLocaiton, Users
# Create your views here.

def LetMeIn(request):
    value = 'Loged'
    if(request.method=='POST'):
        firstName = request.POST.get('fname')
        email = request.POST.get('email')
        if(firstName=='admin'):
            if(email=='admin'):
                print("entered")
                return redirect('map')
        # user = Users(firstName = firstName,email=email)
        # user.save()
        value = 'notLoged'
    return render(request,'index.html')
def getCoordinates(request):
    lattitude = request.GET.get('lattitude')
    longitude = request.GET.get('longitude')
    # cordinates = LiveLocaiton(lattitude=lattitude,longitude=longitude)
    # cordinates.save()
    return render(request,'cordinates.html')

def gMap(request):
    return render(request,'map.html')