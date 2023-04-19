from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
import json

from .models import ProjectDepartment,Project,ProjectMember,Task,PlannedScope,Risk,PlannedLeave

def index(request):
    projectDepartments = ProjectDepartment.objects.all()
    projects = Project.objects.all()
    projectmembers = ProjectMember.objects.all()
    task = Task.objects.all()
    plannedScope = PlannedScope.objects.all()
    risk = Risk.objects.all()
    plannedLeave = PlannedLeave.objects.all()
    context = {
        "is_index" : True,
        "projectDepartments" : projectDepartments,
        "projects" : projects,
        "projectmembers": projectmembers,
        "task":task,
        "plannedScope":plannedScope,
        "risk":risk,
        "plannedLeave":plannedLeave,
    }
    return render(request, 'index.html',context)
