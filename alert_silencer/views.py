from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponseServerError
import requests

# Create your views here.

def index(request):
    req = settings.PROMETHEUS_URL + "/api/v1/rules"
    response = requests.get(req)
    if response.status_code == 200:
        data = response.json()
        return render(request,"alert_silencer/index.html", data)
    else:
        return HttpResponseServerError(response.text)

