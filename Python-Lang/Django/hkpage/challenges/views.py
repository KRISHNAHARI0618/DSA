from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def trigger3(day3):
    return HttpResponse("<h1> Congratulations you have Entered  ... </h2> ")

def trigger1(day1):
    return HttpResponse("<h1> Congratulations you have Configured First Project .. </h2> ")

def trigger2(day2):
    return HttpResponse(" <h1> Congratulations you have entered into February Month ... </h2>")

def trigger4(day4):
    return render(day4,'home.html')
