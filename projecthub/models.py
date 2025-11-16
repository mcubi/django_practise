from django.db import models
from django.contrib.auth.models import User


#################################### PROJECT MODEL #####################################

class Project(models.Model):
    name = models.CharField(max_length=255)
    
    # This attrib mustn't be declared at form fields... // filter for projects on personal page!
    principal_owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='projects') # (1:N)
    
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    propic = models.ImageField(default='default_project.png', blank=True) # DEUD! @ could I relate propics default with 'PROFILE.PROPIC' ? 
    
    # Second generation attributes:
    technologies_used = models.TextField(blank=True)
    repository_url = models.URLField(blank=True) # URL to the project

    # DEUD! @ could I implement later relations with other users ? 
        
    # Third generation attributes:
    # colaborators = ?? Get profile
    # sponsors? = ?? 
    
    # filter attrib (function: 'show_project')
    slug = models.SlugField(unique=True) # DEUD! @ could this come from the username ?

    def __str__(self):
        return self.name
    
    
    
    
#################################### TASK MODEL #####################################
    
    
# DEUD! @ could use Task model so it splits a project in some parts ?
# REL = 1:N // 1 PROJECT, N TASKS (edited)

class Task(models.Model):
    project = models.ForeignKey(Project, related_name='tasks', on_delete=models.CASCADE) # (1:N)
    title = models.CharField(max_length=255)
    description = models.TextField()
    due_date = models.DateField()
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title
    
# @ACLARATION WARN FOR RELATIONS:  // NOTICE <> AND [] ARE SEPARATORS ONLY; NOT SYNTAX AVAIABLE!

# CASE 1:1 => [ <var_name = models.OneToOneField><(Origin, OPTIONS, keyName)> ]

# CASE 1:N => [ <var_name = models.ForeignKey><(Origin, OPTIONS, keyName)> ]

# CASE N:M => [ <var_name = models.ManyToManyField><(Pointer)>]
