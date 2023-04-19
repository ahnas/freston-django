
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
        return str(self.title)

class ProjectMember(models.Model):
    project = models.ForeignKey("Project", on_delete=models.CASCADE)
    member = models.CharField(max_length=120,unique=True)

    def __str__(self):
        return str(self.member)

class Task(models.Model):
    project = models.ForeignKey("Project", on_delete=models.CASCADE)
    task = models.CharField(max_length=1000,unique=True)

    class Meta:
        verbose_name = ('Main Highlights/Achievements')
        verbose_name_plural = ('Main Highlights/Achievements')

    def __str__(self):
        return str(self.task)



