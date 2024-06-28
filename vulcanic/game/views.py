from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def index(request):
    if "counter" not in request.session:
        request.session["counter"] = 0
    return render(request, "game/index.html", {
        "counter": request.session["counter"]
    })

@csrf_exempt
def save(request):
    if request.method != "POST":
        return JsonResponse({"message": "POST request required."}, status=400)

    # Check recipient emails
    data = json.loads(request.body)
    counter = data.get("counter")
    request.session["counter"] = int(counter)

    return JsonResponse({"message": "Counter saved succeesss"}, status=200)
