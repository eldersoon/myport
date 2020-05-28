from django.db import models

# Create your models here.


class Project(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=255)
    tech = models.TextField(max_length=255)
    image = models.ImageField(upload_to='projects_img', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # Display a name in admin
    def __str__(self):
        return self.title
