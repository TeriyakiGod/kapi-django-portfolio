# portfolio/views.py
from django.shortcuts import render
from django.apps import apps

def index(request):
    # Get all installed apps
    installed_apps = [
        {
            "name": app.verbose_name,   # Human-readable name
            "label": app.label,
            "url": app.label + ":index",
            "description": app.description,
        }
        for app in apps.get_app_configs()
        if not app.name.startswith("django.")  # Exclude built-in Django apps
        if not app.name.startswith("django_")
        if not app.name == "app"
        if not app.name == "geoip2"
    ]
    
    return render(request, "index.html", {"installed_apps": installed_apps})
