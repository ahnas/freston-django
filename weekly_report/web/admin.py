from django.contrib import admin
from .models import ProjectDepartment,Project


# Register your models here.


admin.site.register(ProjectDepartment)

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('projectDepartments','title')