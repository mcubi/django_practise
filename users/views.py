from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


def register(request):
    
    if request.method == 'POST':
        premade_form = UserCreationForm(request.POST)
        if premade_form.is_valid():
            user = premade_form.save()
            login(request, user)
            return redirect('homepage')
    else:
        premade_form = UserCreationForm()
    return render(request, 'users/register.html', {'premade_form': premade_form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('homepage')
    else:
        form = AuthenticationForm()
    return render(request, 'users/login.html', {'form': form})

def logout_user(request):
 if request.method == 'POST':
    logout(request)
 return redirect('homepage')

