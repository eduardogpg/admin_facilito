#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from django.db import models
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
		if Project.objects.filter(title = self.title).exclude(pk=self.id).exists():
			raise ValidationError('El proyecto ya se encuentra registrado.')

	def save(self, *args, **kwargs):
		self.validate_unique()
		self.slug = self.title.replace(" ", "_").lower()
		super(Project, self).save(*args, **kwargs)

	def get_format_date(self):
		return "Eduardo Ismael García Pérez"
