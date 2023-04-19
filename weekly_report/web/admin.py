from django.contrib import admin
from .models import ProjectDepartment,Project,ProjectMember


# Register your models here.


admin.site.register(ProjectDepartment)

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title','projectDepartments')

@admin.register(ProjectMember)
class ProjectMemberAdmin(admin.ModelAdmin):
    list_display = ('member','project')