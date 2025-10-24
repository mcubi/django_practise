from django.shortcuts import render
from app1.models import Person
from .models import User

def my_app(request) :
    person_list = Person.objects.all()
    users = User.objects.all()
    return render(request, 'app1/home.html', { 'persons': person_list, 'users': users })
    
def person_page(request, slug):
    person = Person.objects.get(slug=slug)
    return render(request, 'app1/person.html', {'person' : person})


