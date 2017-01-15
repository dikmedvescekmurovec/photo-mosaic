from django.test import TestCase
from projects.models import Project, Comment
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import timedelta

# Create your tests here.
class ProjectTestCase(TestCase):

	def setUp(self):
		self.user = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
		self.p_recent = Project.objects.create(project_name="P", project_owner=self.user, project_text="test", 
			project_funded=100, project_needed=200, 
			project_rating=3.5, pub_date=timezone.now(), random="asd")
		self.p_late = Project.objects.create(project_name="P", project_owner=self.user, project_text="test", 
			project_funded=150, project_needed=200, 
			project_rating=3.5, pub_date=timezone.now() - timedelta(days=10), random="asd")
	
	
	def test_project_is_recent(self):
		self.assertEqual(self.p_recent.is_recent(), True)
		self.assertEqual(self.p_late.is_recent(), False)
		
	def test_project_percentage(self):
		self.assertEqual(self.p_recent.percentage(), 50)
		self.assertEqual(self.p_late.percentage(), 75)
		
class CommentTestCase(TestCase):
	def setUp(self):
			self.user = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
			self.p_recent = Project.objects.create(project_name="P", project_owner=self.user, project_text="test", 
				project_funded=100, project_needed=200, 
				project_rating=3.5, pub_date=timezone.now(), random="asd")
			self.c_recent = Comment.objects.create(project=self.p_recent, comment_text="test", 
				comment_owner=self.user, pub_date=timezone.now())
			self.c_late = Comment.objects.create(project=self.p_recent, comment_text="test", 
				comment_owner=self.user, pub_date=timezone.now() - timedelta(days=10))
				
	def test_comment_is_recent(self):
		self.assertEqual(self.c_recent.is_recent(), True)
		self.assertEqual(self.c_late.is_recent(), False)