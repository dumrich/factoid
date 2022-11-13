from django.shortcuts import render
from django.http import HttpResponse

#TODO: CBV
def index(request):
    return HttpResponse("Factoid index page")
    
