from django.shortcuts import render, redirect
from datetime import  datetime
from Home.models import Contact
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


def index(request):
    if request.user.is_anonymous:
        return redirect("/login")
    return render(request, "index.html")

def destinations(request):
    return render(request,"destinations.html")

def konkan(request):
    return render(request, "map1.html")

def ratnagiri(req):
    return render(req, "dest/ratnagiri.html")


def raigad(req):
    return render(req, "dest/raigad.html")


def mumbai(req):
    return render(req, "dest/mumbai.html")


def sindhudurg(req):
    return render(req, "dest/sindhudurg.html")

def contact(req):
    if req.method == "POST":
        name= req.POST.get('name')
        email= req.POST.get('email')
        text= req.POST.get('text')
        contact= Contact(name=name ,email= email,text = text, date= datetime.today())
        contact.save()
        messages.success(req,"your message has been sent!")
    return render(req, "contact.html")

def loginUser(request):
    if request.method== "POST":
        uname= request.POST.get("username")
        psw= request.POST.get("password")


        user = authenticate(username= uname, password=psw)
        if user is not None:
            login(request,user)
            return redirect('/')
    
        else:
            return render(request, "login.html")
    

    return render(request, "login.html")

def logoutUser(request):
    logout(request)
    return redirect("/login")

def signUp(request):
    
    if request.method== "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect("login")

    else:
        form= UserCreationForm()

    

    return render(request,"signup.html", {'form':form})



# Create your views here.
