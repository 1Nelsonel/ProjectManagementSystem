from django.shortcuts import render

# Create your views here.

# views.py
from django.shortcuts import render
from django.http import HttpResponse

from .models import Project, Task, TeamMember

def project_list(request):
    projects = Project.objects.all()
    context = {'projects': projects}
    return render(request, 'base/project_list.html', context)

def project_detail(request, pk):
    project = Project.objects.get(pk=pk)
    tasks = Task.objects.filter(project=project)
    team_members = TeamMember.objects.filter(project=project)
    context = {
        'project': project,
        'tasks': tasks,
        'team_members': team_members,
    }
    return render(request, 'base/project_detail.html', context)

def task_create(request, pk):
    project = Project.objects.get(pk=pk)
    # Create a new task and associate it with the project
    task = Task(project=project, name=request.POST['name'], 
    description=request.POST['description'], 
    status=request.POST['status'], 
    start_date=request.POST['start_date'], 
    end_date=request.POST['end_date'])
    task.save()
    return HttpResponse('Task created!')

def task_update(request, pk):
    task = Task.objects.get(pk=pk)
    task.status = request.POST['status']
    task.save()
    return HttpResponse('Task updated!')
