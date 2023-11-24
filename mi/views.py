from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse



def rohit(request):
    return render(request,'rohit.html')

def hari(request):
    return HttpResponse('<h1> boom boom </h1>')
