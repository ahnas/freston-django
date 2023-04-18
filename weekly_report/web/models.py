
from django.db import models
from django.db.models.fields import DateField, SlugField
from django.urls import reverse

# Create your models here.

class ProjectDepartment(models.Model):
    title = models.CharField(max_length=120,unique=True)

    def __str__(self):
        return str(self.title)

class Project(models.Model):
    projectDepartments = models.ForeignKey("ProjectDepartment", on_delete=models.CASCADE)
    title = models.CharField(max_length=120,unique=True)

    def __str__(self):
        return str(self.projectDepartments.title)