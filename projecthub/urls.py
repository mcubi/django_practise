from django.urls import path
from . import views

app_name = 'projecthub'

urlpatterns = [
    path('', views.show_hub, name='show_hub'),
    path('<slug:slug>/', views.show_project, name='show_project'),
]