

from django.http import HttpResponse
from listings.models import Band
from django.shortcuts import render

def hello(request):
    bands = Band.objects.all()
    return render(request,
                  'listings/hello.html',
                  {'bands': bands})

def about(request):
    return HttpResponse("<h1>À propos</h1><p> Nous adorons merch !</p>")

def contact(request):
    return HttpResponse("<h1>Contact</h1><p> Contact</p>")

def listings(request):
    return HttpResponse("<h1>Listings</h1><p> Formulaire de listings</p>")

def paleb(request):
    return HttpResponse("<h1>paleb</h1><p> page paleb</p>")