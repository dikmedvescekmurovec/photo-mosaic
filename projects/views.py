from django.shortcuts import render, get_object_or_404
from django.template import loader
from .models import Project, Comment
from django.contrib.auth.models import User
from django.http import *
from django.shortcuts import render_to_response,redirect
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.utils import timezone
import logging

logger = logging.getLogger(__name__)

def index(request):
	logger.info("User " + str(request.user) + " accessed index.")
	latest_projects = Project.objects.order_by('-pub_date')[:5]
	context = {
		'title': "Projects",
		'latest_projects': latest_projects
		}
	return render(request, 'projects/index.html', context)
	
def new(request):
	projects = Project.objects.all()
	new_projects = []
	for project in projects:
		if project.is_recent():
			new_projects.append(project)
	context = {
		'title': "New Projects",
		'latest_projects': new_projects
	}
	return render(request, 'projects/index.html', context)

	
def hot(request):
	projects = Project.objects.all()
	new_projects = []
	for project in projects:
		if project.project_rating > 4:
			new_projects.append(project)
	context = {
		'title': "Hot Projects",
		'latest_projects': new_projects
	}
	return render(request, 'projects/index.html', context)

		
def trending(request):
	projects = Project.objects.all()
	new_projects = []
	for project in projects:
		if project.project_rating > 3:
			new_projects.append(project)
	context = {
		'title': "Trending Projects",
		'latest_projects': new_projects
	}
	return render(request, 'projects/index.html', context)
def project(request, project_id):
	project = get_object_or_404(Project, pk=project_id)
	return render(request, 'projects/project.html', {'project': project})

def delete_project(request, project_id):
	logger.info("Project " + str(project_id) + " deleted by " + str(request.user) + ".")
	get_object_or_404(Project, pk=project_id).delete()	
	return render(request, 'projects/index.html')
	
def delete_comment(request, comment_id):
	logger.info("Comment " + str(project_id) + " deleted by " + str(request.user) + ".")
	get_object_or_404(Comment, pk=comment_id).delete()	
	return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
	
#Check if user already exists before trying to register
def register(request):
	if request.POST:
		username = request.POST['username']
		email = request.POST['email']
		password = request.POST['password']
		repassword = request.POST['repassword']
		if password == repassword:
			user = User.objects.create_user(username, email, password)
			user.save()
			user = authenticate(username=username, password=password)
			login(request, user)
			return render(request, 'projects/index.html')
		else:
			return render(request, 'projects/register.html', {'message': "Password mismatch."})		
	return render(request, 'projects/register.html')

def logout_user(request):
	logout(request)
	return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
	
def login_user(request):
	if request.POST:
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username, password=password)
		if user is not None:
			login(request, user)
			return render(request, 'projects/index.html')
		else:
			return render(request, 'projects/login.html', {'message': "Wrong username or password"})
	return render(request, 'projects/login.html')

def user(request, user_id):
	viewed_user = get_object_or_404(User, pk=user_id)
	return render(request, 'projects/user.html', {'viewed_user': viewed_user})
	
def comment(request, project_id):
	if request.POST:
		comment_project = get_object_or_404(Project, pk=project_id)
		comment = Comment(project=comment_project, 
					comment_text = request.POST['comment-input-text'],
					comment_owner = request.user, pub_date = timezone.now())
		comment.save()
		return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
	return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
		
		
		
		
		
		
		
		
		
		
		
		