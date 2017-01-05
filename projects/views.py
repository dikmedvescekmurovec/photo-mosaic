from django.shortcuts import render, get_object_or_404
from django.template import loader
from .models import Project


def index(request):
	latest_projects = Project.objects.order_by('-pub_date')[:5]
	context = {
		'latest_projects': latest_projects
		}
	return render(request, 'projects/index.html', context)

def project(request, project_id):
	project = get_object_or_404(Project, pk=project_id)
	return render(request, 'projects/project.html', {'project': project})