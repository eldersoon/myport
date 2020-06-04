from django.db import models

# Create your models here.


class Home(models.Model):
    title = models.CharField(max_length=55)
    sub_line_title = models.CharField(max_length=30, null=True, blank=True)
    subtitle = models.TextField(max_length=255)
    image = models.ImageField(upload_to='home_img', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
