# admin.py
from django.contrib import admin

from .models import Project, Task, TeamMember

admin.site.register(Project)
admin.site.register(Task)
admin.site.register(TeamMember)
