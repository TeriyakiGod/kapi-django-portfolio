import datetime
from django.shortcuts import render
import requests
from django.contrib.gis.geoip2 import GeoIP2

def get_weather_data(lat, lon):
    url = f'https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current=temperature_2m,relative_humidity_2m,is_day,rain,wind_speed_10m'
    response = requests.get(url)
    return response.json()

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def get_location(request):
    g = GeoIP2()
    ip = get_client_ip(request)
    if ip == "127.0.0.1":
        ip="kacperochnik.eu"
    location = g.city(ip)
    return location

def forecast(request):
    location = get_location(request)
    data = get_weather_data(location['latitude'], location['longitude'])
    timestamp = data['current']['time']
    time = datetime.datetime.strptime(timestamp, '%Y-%m-%dT%H:%M')
    time_string = time.strftime('%Y-%m-%d %H:%M:%S')
    
    # Extract important data
    weather_info = {
        'time': time_string,
        'city': location['city'],
        'country': location['country_name'],
        'temperature': data['current']['temperature_2m'],
        'humidity': data['current']['relative_humidity_2m'],
        'is_day': data['current']['is_day'],
        'rain': data['current']['rain'],
        'wind_speed': data['current']['wind_speed_10m'],
    }
    
    return render(request, 'weather/app.html', {'weather_info': weather_info})