from django.contrib import admin
from .models import ProjectDepartment,Project,ProjectMember,Task,PlannedScope,Risk,PlannedLeave


# Register your models here.


admin.site.register(ProjectDepartment)

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('id','title','projectDepartments')

@admin.register(ProjectMember)
class ProjectMemberAdmin(admin.ModelAdmin):
    list_display = ('member','project')

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('task','project')

@admin.register(PlannedScope)
class PlannedScopeAdmin(admin.ModelAdmin):
    list_display = ('project','details')

@admin.register(Risk)
class RiskAdmin(admin.ModelAdmin):
    list_display = ('project','risk')

@admin.register(PlannedLeave)
class PlannedLeaveAdmin(admin.ModelAdmin):
    list_display = ('project','member','date')