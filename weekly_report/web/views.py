from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
import json

from .models import ProjectDepartment,Project

def index(request):
    projectDepartments = ProjectDepartment.objects.all()
    obj = Project.objects.filter()
    projects = Project.objects.all()
    context = {
        "is_index" : True,
        "projectDepartments" : projectDepartments,
        "projects" : projects,
    }
    return render(request, 'index.html',context)
