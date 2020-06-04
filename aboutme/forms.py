from django.forms import ModelForm
from .models import Aboutme


class AboutmeForm(ModelForm):
    class Meta:
        model = Aboutme
        fields = ['title', 'description', 'image']
        exclude = ('created_at', 'updated_at')
