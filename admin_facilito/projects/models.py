#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from django.db import models
from status.models import Status

import datetime

class Project(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	title = models.CharField(max_length=50)
	description = models.TextField ()
	dead_line = models.DateField()
	create_date = models.DateField(default=datetime.date.today)
	slug = models.CharField(max_length=50, default="")

	def __str__(self):
		return self.title

	def validate_unique(self, exclude=None):
		self.slug = self.create_slug_field(self.title)
		if Project.objects.filter(slug = self.slug).exclude(pk=self.id).exists():
			raise ValidationError('El proyecto ya se encuentra registrado!')
		super(Project, self).clean()
	
	def create_slug_field(self, value):
		return value.lower().replace(" ", "-")

	def get_status(self):
		return self.projectstatus_set.last().status


class ProjectStatus(models.Model):
	project = models.ForeignKey(Project, on_delete=models.CASCADE)
	status = models.ForeignKey(Status)
	create_date = models.DateField(default=datetime.date.today)
	
	def __str__(self):
		return "{} - {}".format(self.project.title, self.status.title)





