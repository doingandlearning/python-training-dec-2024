from django.shortcuts import render
from django.http import JsonResponse
import requests


API_KEY="0de6bc7ec1efaff74b56d2bab3b38f6e"
# Create your views here.

in_memory_cache = {}

def get_weather(request):
    city = request.GET.get("city", "Edinburgh")

    if "," in city:
        cities = city.split(",")
        print(cities)
        cities_data = [
            get_weather_of_city(city) for city in cities
        ]
        return JsonResponse({"data":cities_data})
    # return JsonResponse(data)
    # Extract key information
    else:
        return JsonResponse(get_weather_of_city(city))

def get_weather_of_city(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    if in_memory_cache.get(city):
        print("returning from cache")
        return in_memory_cache[city]
    # Fetch weather data from OpenWeatherMap
    try:
        response = requests.get(url)
        if response.status_code != 200:
            raise Exception(f"Exception raised at {url} with status code {response.status_code}")
    except Exception as exp:
        print(exp)
        return JsonResponse({"error": "something went wrong"}, status=400)

    data = response.json()
    return {
        "city": data["name"],
        "temperature": data["main"]["temp"],
        "description": data["weather"][0]["description"]
    }