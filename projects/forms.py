from django.forms import ModelForm
from .models import Project


class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'description', 'tech', 'image']
        exclude = ('created_at', 'updated_at')
