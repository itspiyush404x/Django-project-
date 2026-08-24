from django.shortcuts import render
from django.http import HttpResponse
# from hello_world.data import forms
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
@csrf_exempt
def hello(request):
    if request.method == "POST":
        name = request.POST.get("name","Unknown")
        return HttpResponse(f"Hello {name}!")
    return HttpResponse("sent post request")

def hello_piyush(request):
    return HttpResponse("Hello Piyush")

def hello_jatin(request):
    return HttpResponse("Hello Jatin")


    
