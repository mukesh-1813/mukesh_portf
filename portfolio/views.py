from django.shortcuts import render, get_object_or_404
from .models import Project, Resume, Profile

def home(request):

    featured_projects = Project.objects.filter(is_featured=True)[:6]
    if not featured_projects.exists():
        featured_projects = Project.objects.all()[:3]
    
    active_resume = Resume.objects.filter(is_active=True).first()
    profile = Profile.objects.first()
    
    # Skills are structured as categories for the template
    skills = [
        {"category": "Backend Development", "tags": ["Django", "Django REST Framework (DRF)", "REST API Development"]},
        {"category": "Programming", "tags": ["Python", "Core Java","C"]},
        {"category": "Frontend", "tags": ["HTML", "CSS", "JavaScript"]},
        {"category": "Data Structures", "tags": ["Arrays", "Strings", "Hashing","Data Structures & Algorithms"]},
        {"category": "Tools", "tags": ["Git (Basic)", "VS Code"]},
    ]
    
    context = {
        'featured_projects': featured_projects,
        'active_resume': active_resume,
        'profile': profile,
        'skills': skills,
    }
    return render(request, 'portfolio/home.html', context)



def project_list(request):
    projects = Project.objects.all()
    profile = Profile.objects.first()
    return render(request, 'portfolio/project_list.html', {'projects': projects, 'profile': profile})

def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    profile = Profile.objects.first()
    # Splitting tech_stack by comma for tags
    tech_tags = [tag.strip() for tag in project.tech_stack.split(',')]
    return render(request, 'portfolio/project_detail.html', {
        'project': project, 
        'tech_tags': tech_tags,
        'profile': profile
    })

def contact(request):
    active_resume = Resume.objects.filter(is_active=True).first()
    profile = Profile.objects.first()
    return render(request, 'portfolio/contact.html', {'active_resume': active_resume, 'profile': profile})

from django.http import HttpResponse
def health_check(request):
    return HttpResponse("OK")


