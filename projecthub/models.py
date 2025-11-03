from django.db import models

class Project(models.Model):
    name = models.CharField(max_length=255)
    principal_owner = models.CharField(max_length=255) # DEUD: This should be a ForeignKey to a User model ! 1 principal owner - n projects; 1 p 1 o
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    propic = models.ImageField(default='default_project.png', blank=True) # DEUD: This should be configured through User class !
    slug = models.SlugField(unique=True) # DEUD: This should be auto-generated from the name field !
    
    # DEUD: ADD THE FOLLOWING FIELDS: ['repository_url', 'live_demo_url', 'technologies_used']
    
    # DEUD: Add colaborators and sponsor fields later !

    def __str__(self):
        return self.name
    
# DEUD: Model created cause of exercise ! @ think utility or delete later !

class Task(models.Model):
    project = models.ForeignKey(Project, related_name='tasks', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    due_date = models.DateField()
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title
