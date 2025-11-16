from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm # no more original register form !
from django.contrib.auth.decorators import login_required
from projecthub.models import Project
from .forms import ProjectForm

from .forms import CustomUserCreationForm # @ form with email added!

# REGISTER VIEW
def register(request):
    
    if request.method == 'POST':
        premade_form = CustomUserCreationForm(request.POST)
        if premade_form.is_valid():
            user = premade_form.save()
            
            login(request, user) # login the user automatically
            return redirect('homepage') # DEUD! @ could you make it redirect user to personal page once it's finished? 
    else:
        premade_form = CustomUserCreationForm()
    return render(request, 'users/register.html', {'premade_form': premade_form})


# LOGIN VIEW
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        
        if form.is_valid():
            login(request, form.get_user()) # login user
            
            if 'next' in request.POST:
                return redirect(request.POST.get('next')) # case he wanted to acces to a page previously = save url 
                                                          # and pass it so he can be redirected to it
            else:
                return redirect('homepage')
    else:
        form = AuthenticationForm()
    return render(request, 'users/login.html', {'form': form})


# LOGOUT VIEW
def logout_user(request):
 if request.method == 'POST':
    logout(request)
 return redirect('homepage')


# PERSONAL PAGE VIEW WITH THE PROJECTS AND THE CREATION OF THEM VIA FORM

# DEUD! @ could I turn this page into a personal displayer? @upLastDeud!
@login_required(login_url='users:login')
def personal_projects(request):
    user_projects = Project.objects.filter(principal_owner=request.user)
    
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            
            # DEUD! @ could I turn this sht into a foreign key at projecthub/models.py ? thx
            new_project = form.save(commit=False) 
            new_project.principal_owner = request.user
            new_project.save()
            return redirect('users:personal_page')
        
    else:     
        form = ProjectForm()
        
    return render(request, 'users/personalProjects.html', {'user_projects': user_projects, 'form': form})
   
