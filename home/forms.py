from django.forms import ModelForm
from .models import Home


class HomeForm(ModelForm):
    class Meta:
        model = Home
        fields = ['title', 'sub_line_title', 'subtitle', 'image']
        exclude = ('created_at', 'updated_at')
