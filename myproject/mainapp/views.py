from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return render(request, "index.html")
def slide(request):
    return render(request, "slide.html")
def vikidb(request):
    return HttpResponse("Ok")
def slider2(request):
    return render(request, "slider2.html")
