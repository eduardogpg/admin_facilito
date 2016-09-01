from django.contrib.auth.models import User
from .models import Project
from .models import ProjectStatus
from .models import PermissionProject
from status.models import Status

from django.shortcuts import render

from django.views.generic import CreateView
from django.views.generic import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import DeleteView
from django.views.generic.edit import UpdateView
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

from django.core.urlresolvers import reverse_lazy

from django.shortcuts import get_object_or_404
from .forms import CreateProjectForm
from .forms import EditProjectForm
from status.forms import StatusChoiceForm

from django.contrib import messages
from django.http import HttpResponseRedirect
from django.contrib.messages.views import SuccessMessageMixin

from django.core.exceptions import ObjectDoesNotExist
from django.views.decorators.http import require_http_methods
from django.shortcuts import redirect
import json
"""
Class
"""

class ShowClass(DetailView):
	model = Project
	template_name = 'project/show.html'

class CreateClass(CreateView, LoginRequiredMixin):
	login_url = 'client:login'
	template_name = 'project/create.html'
	model = Project
	form_class = CreateProjectForm

	def form_valid(self, form):
		self.object = form.save(commit = False)
		self.object.user = self.request.user
		self.object.save()
		self.object.projectstatus_set.create(status = Status.dafault_value() )
		return HttpResponseRedirect( self.project_show() ) 

	def project_show(self):
		return reverse_lazy('project:show', kwargs={'slug': self.object.slug})

class ListClass(ListView, LoginRequiredMixin):
	login_url = 'client:login'
	template_name = 'project/own.html'

	def get_queryset(self):
		return Project.objects.filter(user=self.request.user).order_by('dead_line')
	
class EditClass(LoginRequiredMixin, UpdateView, SuccessMessageMixin):
	login_url = 'client:login'
	success_url =  reverse_lazy('client:dashboard')

	template_name = 'project/edit.html'
	model = Project
	form_class = EditProjectForm
	fail_url = reverse_lazy('')
	success_url = reverse_lazy('client:dashboard')
	success_message = "El proyecto ha sido actualizado exitosamente."

	def dispatch(self, request, *args, **kwargs):
		obj = self.get_object()
		if obj.user != self.request.user:
			return HttpResponseRedirect( self.get_success_url() ) 
		return super(EditClass, self).dispatch(request, *args, **kwargs)

	def prepare_fake_url(self):
		return reverse_lazy('project:show', kwargs={'slug': self.object.slug})

@login_required( login_url = 'client:login' )
def edit(request, slug = ''):
	project = get_object_or_404(Project, slug=slug)

	if request.user.id != project.user_id:
		return redirect('client:dashboard')

	form_project = EditProjectForm(request.POST or None, instance = project)
	form_status = StatusChoiceForm(request.POST or None, 
																	initial = {'status':  project.get_id_status() }
																)
	
	if request.method == 'POST':
		if form_project.is_valid() and form_status.is_valid():
			form_project.save()
			selection = form_status.cleaned_data['status'].id
			
			if selection != project.get_status().status_id:
				project.projectstatus_set.create(status_id = selection)
			messages.success(request, 'Datos actualizados correctamente')

	context = {
		'project' : project,
		'form_project' : form_project,
		'form_status': form_status
	}
	return render(request, 'project/edit.html', context)

@login_required( login_url = 'client:login' )
def collaboration(request, slug=''):
	project = get_object_or_404(Project, slug=slug)
	context = {
		'project' : project
	}
	return render(request, 'project/collaboration.html', context)

@csrf_exempt
def add_collaboration(request, slug='', username=''):
	user = get_object_or_none(User, username = username)
	project = get_object_or_none(Project, slug = slug)
	if user is not None and project is not None:
		project.projectuser_set.create(user = user, permission = PermissionProject.default_value() )

	return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def get_object_or_none(object_model, **kwargs):
	try:
		return object_model.objects.get(**kwargs)
	except ObjectDoesNotExist:
		return None
