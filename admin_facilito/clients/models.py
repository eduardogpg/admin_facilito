from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
        
class Client(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	bio = models.TextField(max_length = 200, blank=True, default = "" )
	job = models.CharField(max_length = 50, blank=True, default = "")

	def __str__(self):
		return self.user.username

class SocialNetwork(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	facebook = models.URLField( blank=True )
	twitter = models.URLField( blank=True )
	github = models.URLField( blank=True )

	def __str__(self):
		return self.user.username
