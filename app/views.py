# portfolio/views.py
from django.shortcuts import render
from django.apps import apps

def index(request):
    # Get all installed apps
    installed_apps = [
        {
            "name": app.verbose_name,   # Human-readable name
            "description": app.description,
            "label": app.label,
            "url": app.label + ":index",
        }
        for app in apps.get_app_configs()
        if not app.name.startswith("django.")  # Exclude built-in Django apps
        if not app.name.startswith("django_")
        if not app.name == "app"
    ]
    
    return render(request, "index.html", {"installed_apps": installed_apps})
