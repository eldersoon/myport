from django.forms import ModelForm
from .models import Tech


class TechForm(ModelForm):
    class Meta:
        model = Tech
        fields = ['tech', 'icon']
        exclude = ('created_at', 'updated_at')
