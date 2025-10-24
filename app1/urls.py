from django.urls import path
from . import views

app_name = 'people'

urlpatterns = [
    path('', views.my_app, name="home"),          
    path('<slug:slug>/', views.person_page, name="person"),
    
]
