#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from django.db import models
from django.utils import timezone

from status.models import Status

class Project(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	title = models.CharField(max_length=50)
	description = models.TextField ()
	dead_line = models.DateField()
	create_date = models.DateTimeField(default = timezone.now)
	slug = models.CharField(max_length=50, default="")

	def __str__(self):
		return self.title

	def validate_unique(self, exclude=None):
		self.slug = self.create_slug_field(self.title)
		if Project.objects.filter(slug = self.slug).exclude(pk=self.id).exists():
			raise ValidationError('El proyecto ya se encuentra registrado!')
		super(Project, self).clean()
	
	def has_permission(self, user):
		return self.user == user or self.has_admin_permission(user)

	def has_admin_permission(self, user):
		return self.projectuser_set.filter(user=user, permission_id = 1).count() > 0

	def create_slug_field(self, value):
		return value.lower().replace(" ", "-")

	def get_status(self):
		return self.projectstatus_set.last()

	def get_id_status(self):
		return self.projectstatus_set.last().status.id		

class ProjectStatus(models.Model):
	project = models.ForeignKey(Project)
	status = models.ForeignKey(Status)
	create_date = models.DateTimeField(default = timezone.now)
	
	def __str__(self):
		return "{} - {}".format(self.project.title, self.status.title)

class PermissionProject(models.Model):
	title = models.CharField(max_length=50)
	description = models.TextField()
	level = models.IntegerField()
	active = models.BooleanField(default=True)
	create_date = models.DateTimeField(default = timezone.now)

	@classmethod
	def default_value(cls):
		return cls.objects.get(pk=1)

	def __str__(self):
		return self.title

class ProjectUser(models.Model):
	project = models.ForeignKey(Project)
	user = models.ForeignKey(User)
	permission = models.ForeignKey(PermissionProject)
	create_date = models.DateTimeField(default = timezone.now)
	update_date = models.DateTimeField(default = timezone.now)

	def get_user(self):
		return self.user

	def __str__(self):
		return self.user.username