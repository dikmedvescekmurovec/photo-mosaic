from django.db import models
import datetime
from django.utils import timezone

from django.contrib.auth.models import User

class Project(models.Model):

	project_name = models.CharField(max_length=200)
	project_owner = models.ForeignKey(User, on_delete=models.CASCADE)
	project_text = models.CharField(max_length=5000)
	project_funded = models.DecimalField(max_digits = 20, decimal_places=2)
	project_needed = models.DecimalField(max_digits = 20, decimal_places=2)
	project_rating = models.DecimalField(max_digits = 3, decimal_places=2)
	pub_date = models.DateTimeField('date published')
	random = models.CharField(max_length=20)

	def __str__(self):
		return self.project_name
		
	def is_recent(self):
		return self.pub_date >= timezone.now() - datetime.timedelta(days=3)
		
	def percentage(self):
		return 100*(self.project_funded/self.project_needed)
		
class Comment(models.Model):
	def __str__(self):
		return self.comment_text
		
	project = models.ForeignKey(Project, on_delete=models.CASCADE)
	comment_text = models.CharField(max_length=500)
	comment_owner = models.ForeignKey(User, on_delete=models.CASCADE)
	pub_date = models.DateTimeField('date published')
	
	def is_recent(self):
		return self.pub_date >= timezone.now() - datetime.timedelta(days=3)