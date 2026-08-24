from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json



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

@csrf_exempt
def form(request):
    if request.method == "POST":
        try:
            with open(r"C:\Users\C C\OneDrive\Desktop\coaching projects\projects\first_django_project\Backend\main\data.json", "r") as f:
                file_data = json.load(f)
        except json.JSONDecodeError:
            file_data = {}
        
        index = max([int(i) for i in file_data]) + 1
        file_data.update({str(index):json.loads(request.body)})

        with open(r"C:\Users\C C\OneDrive\Desktop\coaching projects\projects\first_django_project\Backend\main\data.json", "w") as f:
            json.dump(file_data, f, indent=4)
    
    return HttpResponse("Form submitted successfully!")

        

        
            




    
