from django import forms
from projecthub import models
from django.contrib.auth.forms import UserCreationForm # Import the form to extend it by adding email
from django.contrib.auth.models import User # Model used as Meta

######################### FORM @ PROJECTS (PROJECTHUB APP): #########################

# (function: 'personal_projects')

class ProjectForm(forms.ModelForm):
    class Meta:
        model = models.Project
        
        # 'principal_owner' not included; it's autofilled at the view 
        
        fields = ['name', 'description', 'start_date', 'end_date', 'propic', 'technologies_used', 'repository_url', 'slug',] 
        
        
######################### FORM @ USER (DJANGO AUTH USER) :: Email extension #########################

# (function: 'register')
 
class CustomUserCreationForm(UserCreationForm): # 'override' of UserCreationForm to add the email as a new imput field
    email = forms.EmailField(required=True) # Adding the email field as a requirement
    
    class Meta: 
        model = User
        fields = ("username", "email", "password1", "password2") # Fields of Meta::User now include email
        
    def save(self, commit=True):
        user = super().save(commit=False) # Stop the db commit process
        user.email = self.cleaned_data["email"] # Add email for future push
        if commit:
            user.save() # Re-engage
        return user
        
        

