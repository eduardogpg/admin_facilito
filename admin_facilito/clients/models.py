from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User

class Client(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	bio = models.TextField(max_length = 200)
	job = models.CharField(max_length = 50)

	def __str__(self):
		return self.user.username