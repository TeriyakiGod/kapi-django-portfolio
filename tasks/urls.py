from django.urls import path
from . import views

app_name = 'tasks'

urlpatterns = [
    path('', views.list, name='list'),
    path('<int:id>/', views.detail, name='detail'),
    path('create/', views.create, name='create'),
    path('<int:id>/update/', views.update, name='update'),
    path('<int:id>/delete/', views.delete, name='delete'),
    path('<int:id>/toggle/', views.toggle_task_status, name='toggle_task_status'),
]