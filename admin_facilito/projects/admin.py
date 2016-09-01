from django.contrib import admin
from .models import Project
from .models import ProjectStatus
from .models import PermissionProject

class ProjectStatusInLine(admin.TabularInline):
	model = ProjectStatus
	can_delete = False
	extra = 0

class ProjectAdmin(admin.ModelAdmin):
    inlines = [
        ProjectStatusInLine,
    ]

admin.site.register(Project, ProjectAdmin)
admin.site.register(PermissionProject)