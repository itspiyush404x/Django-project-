from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
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
    if request.method == "POST":
        file_data = load_Json_data()
        data = json.loads(request.body)
        # check json format amd missing parameters
        for key in ("name", "age", "email"):
            if key not in data or not data[key] and len(data)!=3:
                return JsonResponse({"error":"Invalid Json"}, status=422)
            else: # check for incorrect email
                if "@" not in data["email"]:
                    return JsonResponse({"error":"Invalid Email"}, status=422)
        # checks for duplicate email
        for form in file_data.values():
            if form["email"] == data["email"]:
                return JsonResponse({"error":"User Already Exist"}, status=422)

        if file_data:
            id_ = max([int(i) for i in file_data]) + 1
        else:
            id_ = 1
        
        file_data.update({str(id_):data})

        with open(JSON_DIR, "w") as f:
            json.dump(file_data, f, indent=4)

        return JsonResponse(file_data, status=201)
    else:
        return JsonResponse({"error":"Method Not Allowed"}, status=405)

@csrf_exempt
def update_form(request,id_):
    if request.method in ("PUT", "PATCH"):
        file_data = load_Json_data()
        if id_ not in file_data:
            return JsonResponse({"error":"ID not found"}, status=404)

        if request.method == "PUT":
            data = json.loads(request.body)
            if len(data)!=3:
                return JsonResponse({"error":"Invalid Json"}, status=422)
            for key in ("name", "age", "email"):
                if key not in data:
                    if data[key]:
                        return JsonResponse({"error":"Invalid Json"}, status=422)

            file_data.update({id_:data})
            
        elif request.method == "PATCH":
            data = json.loads(request.body)
            for key in data:
                if key not in ("name", "age", "email"):
                    return JsonResponse({"error":"Invalid Json"}, status=422) 
                file_data[id_].update({key:data[key]})

        with open(JSON_DIR, "w") as f:
            json.dump(file_data, f, indent=4)
        return JsonResponse(file_data, status=200)
    else:
        return JsonResponse({"error":"Method Not Allowed"}, status=405)

@csrf_exempt
def delete_form(request,id_):
    if request.method == "DELETE":
        file_data = load_Json_data()
        if id_ not in file_data:
            return JsonResponse({"error":"ID not found"}, status=404)


        del file_data[id_]

        with open(JSON_DIR, "w") as f:
                json.dump(file_data, f, indent=4)

        return JsonResponse(file_data, status=204)
    else:
        return JsonResponse({"error":"Method Not Allowed"}, status=405)

        


        

        
            




    
