from .models import Project

from django.shortcuts import render

from django.views.generic import CreateView
from django.views.generic import DetailView
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin

from django.core.urlresolvers import reverse_lazy

from .forms import CreateProjectForm

from django.http import HttpResponseRedirect

"""
Class
"""

class CreateClass(CreateView, LoginRequiredMixin):
	login_url = 'client:login'
	success_url =  reverse_lazy('client:dashboard')
	template_name = 'project/create.html'
	model = Project
	form_class = CreateProjectForm

	def form_valid(self, form):
		self.object = form.save(commit = False)
		self.object.user = self.request.user
		self.object.save()
		return HttpResponseRedirect( self.get_success_url() ) 

class ListClass(ListView, LoginRequiredMixin):
	login_url = 'client:login'
	template_name = 'project/own.html'

	def get_queryset(self):
		return Project.objects.filter(user=self.request.user)
	

class ShowClass(DetailView):
	model = Project
	template_name = 'project/show.html'
	slug_field = 'slug'
	slug_url_kwarg = 'slug'




