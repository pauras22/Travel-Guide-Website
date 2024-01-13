from django.contrib import admin

from django.urls import path
from Home import views
urlpatterns = [
    path("" , views.index, name="Home"),
    path("home" , views.index, name="Home"),
    path("destinations" , views.destinations, name="destinations"),
    path("konkan", views.konkan,name="konkan"),

    path("ratnagiri" ,views.ratnagiri, name="ratnagiri"),
    path("raigad" ,views.raigad, name="raigad"),
    path("sindhudurg" ,views.sindhudurg, name="sindhudurg"),
    path("mumbai" ,views.mumbai, name="mumbai"),




    path("contact",views.contact , name="contact" ),
    path("login" , views.loginUser, name="login"),
    path("logout" , views.logoutUser, name="logout"),
    path("signup", views.signUp, name= "signup")
]
