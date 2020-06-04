from django.db import models

# Create your models here.


class Tech(models.Model):
    tech = models.CharField(max_length=30)
    icon = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
