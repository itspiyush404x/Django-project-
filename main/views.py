from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent
JSON_DIR = BASE_DIR / "data.json"
print(JSON_DIR)
    



# Create your views here.
@csrf_exempt
def hello(request):
    if request.method == "GET":
        return HttpResponse("hello world")
    elif request.method == "POST":
        name = request.POST.get("name","Unknown")
        return HttpResponse(f"Hello {name}!")
    return HttpResponse("sent post request")


def load_Json_data():
    try:
        with open(JSON_DIR, "r") as f:
            file_data = json.load(f)
    except json.JSONDecodeError, FileNotFoundError:
        file_data = {}
    return file_data


@csrf_exempt
def submit_form(request):
    file_data = load_Json_data()
    if file_data:
        id_ = max([int(i) for i in file_data]) + 1
    else:
        id_ = 1
    
    file_data.update({str(id_):json.loads(request.body)})

    with open(JSON_DIR, "w") as f:
        json.dump(file_data, f, indent=4)

    return HttpResponse(f"Form submitted successfully! - {file_data.items()}")


@csrf_exempt
def update_form(request,id_):
    file_data = load_Json_data()
    if id_ not in file_data:
        return HttpResponse(f"ERROR: Id-{id_} not found")

    if request.method in ("PUT", "PATCH"):
        if request.method == "PUT":
            file_data.update({id_:json.loads(request.body)})
            
        elif request.method == "PATCH":
            data = json.loads(request.body)
            for key in data:
                file_data[id_].update({key:data[key]})

        with open(JSON_DIR, "w") as f:
            json.dump(file_data, f, indent=4)
        return HttpResponse(f"Form updated successfully! - {file_data.items()}")


@csrf_exempt
def delete_form(request,id_):
    file_data = load_Json_data()
    if id_ not in file_data:
        return HttpResponse(f"ERROR: Id-{id_} not found")


    del file_data[id_]

    with open(JSON_DIR, "w") as f:
            json.dump(file_data, f, indent=4)

    return HttpResponse(f"Form deleted successfully! - {file_data.items()}")

        


        

        
            




    
