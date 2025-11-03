from django import forms
from projecthub import models

class ProjectForm(forms.ModelForm):
    class Meta:
        model = models.Project
        # PERSONAL OWNER IS FILLED AUTOMATICALLY BY THE VIEW
        fields = ['name', 'description', 'start_date', 'end_date', 'propic', 'slug',]