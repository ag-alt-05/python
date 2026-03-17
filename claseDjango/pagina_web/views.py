from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def vista(solicitud):
    return HttpResponse("Hola mundo")
