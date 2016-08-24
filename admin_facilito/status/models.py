#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

class Status(models.Model):
	title = models.CharField(max_length=50)
	description = models.TextField()
	color = models.CharField(max_length=10)
	create_date = models.DateTimeField(default=timezone.now)
	slug = models.CharField(max_length=50)
	active = models.BooleanField(default = True)

	def __str__(self):
		return self.title

	class Meta:
		verbose_name = "Status"
		verbose_name_plural = "Status"
