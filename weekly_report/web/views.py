from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
import json

from .models import ProjectDepartment,Project,ProjectMember,Task

def index(request):
    projectDepartments = ProjectDepartment.objects.all()
    projects = Project.objects.all()
    projectmembers = ProjectMember.objects.all()
    task = Task.objects.all()
    context = {
        "is_index" : True,
        "projectDepartments" : projectDepartments,
        "projects" : projects,
        "projectmembers": projectmembers,
        "task":task,
    }
    return render(request, 'index.html',context)
