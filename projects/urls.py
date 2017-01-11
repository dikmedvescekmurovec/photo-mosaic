from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^(?P<project_id>[0-9]+)/$', views.project, name='project'),
	url(r'^register/', views.register, name='register'),
	url(r'^logout/', views.logout_user, name='logout_user'),
	url(r'^login/', views.login_user, name='login_user'),
	url(r'^user/(?P<user_id>[0-9]+)/$', views.user, name='user'),
	url(r'^(?P<project_id>[0-9]+)/comment/$', views.comment, name='comment'),
]