from django.http import HttpResponse
#from django.shortcuts import render


def home(request): #pylint: disable=unused-argument
    return HttpResponse("Bienvenido a Parque Salitre Mágico")
