from django.shortcuts import render
from django.http import HttpResponse, JsonResponse  
from .models import Project, Task
from django.shortcuts import get_object_or_404, render, redirect
from .forms import CreateNewTask, CreateNewProject 

# Create your views here.
def index(request):
    title = 'Django Title!'
    return render(request, 'index.html', {
        'titulo':title
    })

def hello(request, username):
    return HttpResponse("<h2>Hello %s</h2>" % username)

def about(request):
    username = 'TuUserName'
    return render(request, 'about.html', {
        'username': username
    })

def projects(request):
    # projects = list(Project.objects.values())
    projects = Project.objects.all()
    return render(request,'projects/projects.html', {
        'projects': projects
    })

def tasks(request):
    # task = get_object_or_404(Task)
    tasks = Task.objects.all()
    return render(request, 'tasks/tasks.html', {
        'tasks':tasks
    })

def create_tasks(request):
    if request.method == 'GET':
        return render(request, 'tasks/create_tasks.html', {
            'form': CreateNewTask()
        })
    else: 
        Task.objects.create(title=request.POST['title'],
                            description=request.POST['description'],project_id=2)
        return redirect('tasks')

def create_projects(request):
    if request.method == 'GET':
        return render(request, 'projects/create_project.html',{
            'form': CreateNewProject()
        })
    else: 
        Project.objects.create(name=request.POST["name"])
        redirect('projects')

def project_detail(request, id):
    project = get_object_or_404(Project, id=id)
    tasks = Task.objects.filter(project_id=id) 
    print(id)
    return render(request, 'projects/detail.html', {
        'project': project,
        'tasks': tasks
    })