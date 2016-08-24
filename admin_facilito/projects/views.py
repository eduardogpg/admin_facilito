from .models import Project
from .models import ProjectStatus

from django.shortcuts import render

from django.views.generic import CreateView
from django.views.generic import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import DeleteView
from django.views.generic.edit import UpdateView
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
		self.object.projectstatus_set.create(status_id = 1)
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
	form_status = StatusChoiceForm(request.POST or None)
	
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

