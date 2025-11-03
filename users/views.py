from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from projecthub.models import Project
from .forms import ProjectForm

# REGISTER VIEW
def register(request):
    
    if request.method == 'POST':
        premade_form = UserCreationForm(request.POST)
        if premade_form.is_valid():
            user = premade_form.save()
            
            # LOG THE USER IN AFTER REGISTRATION AND GO HOME
            # DEUD: REDIRECT TO REPO HOSTER FUTURE PAGE !
            login(request, user)
            return redirect('homepage')
    else:
        premade_form = UserCreationForm()
    return render(request, 'users/register.html', {'premade_form': premade_form})


# LOGIN VIEW
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        
        # IF THE FORM IS VALID, LOG THE USER IN
        if form.is_valid():
            login(request, form.get_user())
            
            # REDIRECT TO THE PAGE THE USER WANTED TO ACCESS BEFORE LOGIN OR TO HOMEPAGE
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
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
# DEUD: TRANSFORM INTO A PERSONAL PAGE WITH MORE FUNCTIONALITY :: TRANSPORT THE PROJECT CREATION TO ANOTHER PAGE
@login_required(login_url='users:login')
def personal_projects(request):
    user_projects = Project.objects.filter(principal_owner=request.user.username)
    
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            new_project = form.save(commit=False)
            new_project.principal_owner = request.user.username
            new_project.save()
            return redirect('users:personal_page')
        
    else:     
        form = ProjectForm()
        
    return render(request, 'users/personalProjects.html', {'user_projects': user_projects, 'form': form})
   
