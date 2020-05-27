from django.db import models

# Create your models here.


class Project(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=255)
    tech = models.TextField(max_length=255)
    image = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # display a name in admin
    def __str__(self):
        return self.title
