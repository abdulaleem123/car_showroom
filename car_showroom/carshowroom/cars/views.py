from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Car
from math import ceil
def index(request):
    car_products = Car.objects.all()
    context = {
        'car_products': car_products,
    }
    return render(request, 'cars/index.html', context)

def about(request):
    return HttpResponse("We are at about")

def contact(request):
    return HttpResponse("We are at contact")

def tracker(request):
    return HttpResponse("We are at tracker")

def search(request):
    return HttpResponse("We are at search")

def productView(request):
    return HttpResponse("We are at product view")

def checkout(request):
    return HttpResponse("We are at checkout")

