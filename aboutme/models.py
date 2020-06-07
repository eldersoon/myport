from django.db import models

# Create your models here.


class Aboutme(models.Model):
    title = models.CharField(max_length=55)
    description = models.TextField(max_length=1000)
    image = models.FileField(upload_to='home_img', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
