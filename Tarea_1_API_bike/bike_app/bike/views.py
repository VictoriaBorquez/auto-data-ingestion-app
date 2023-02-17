from django.http import HttpResponse
from django.shortcuts import render
import requests
from bike.models import *

def index(request):
   return HttpResponse("Hello, world. You're at the bike index.")

#def get_data(request):
url = "http://api.citybik.es/v2/networks/bikesantiago"
response = requests.get(url).json()

for extra in response["network"]["stations"]:
   Extra.objects.create(address=extra["extra"]["address"], altitude=extra["extra"]["altitude"], ebikes=extra["extra"]["ebikes"], has_bikes=extra["extra"]["has_ebikes"], last_updated=extra["extra"]["last_updated"], normal_bikes=extra["extra"]["normal_bikes"], payment=extra["extra"]["payment"], payment_terminal=extra["extra"]["payment-terminal"], renting=extra["extra"]["renting"], returning=extra["extra"]["returning"], slots=extra["extra"]["slots"])

Location.objects.create(city=response["network"]["location"]["city"], country=response["network"]["location"]["country"],latitude=response["network"]["location"]["latitude"],longitude=response["network"]["location"]["longitude"])

for station in response["network"]["stations"]:
   Stations.objects.create( name=station["name"], date=station["timestamp"], latitude=station["latitude"], longitude=station["longitude"], free_bikes=station["free_bikes"], empty_slots=station["empty_slots"])

Network.objects.create(company=response["network"]["company"],gbfs_href=response["network"]["gbfs_href"], href=response["network"]["href"],name=response["network"]["name"])
   #return render(request, 'home.html', {'response':response})

def station(request):
   station = Stations.objects.all()
   return render(request, "home.html", {'station':station})