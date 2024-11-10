from django.urls import path
from . import views

app_name = 'shorturl'

urlpatterns = [
    path('', views.shorten_url, name='index'),
    path('<str:short_code>/', views.redirect_to_original, name='redirect_to_original'),
]
