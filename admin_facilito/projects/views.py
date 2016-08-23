from .models import Project

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
	slug_field = 'slug'
	slug_url_kwarg = 'slug'

class CreateClass(CreateView, LoginRequiredMixin):
	login_url = 'client:login'
	template_name = 'project/create.html'
	model = Project
	form_class = CreateProjectForm
	success_url = reverse_lazy('client:dashboard')

	def form_valid(self, form):
		self.object = form.save(commit = False)
		self.object.user = self.request.user
		self.object.save()
		return HttpResponseRedirect( self.get_success_url() ) 

class ListClass(ListView, LoginRequiredMixin):
	login_url = 'client:login'
	template_name = 'project/own.html'

	def get_queryset(self):
		return Project.objects.filter(user=self.request.user).order_by('dead_line')
	
#http://stackoverflow.com/questions/18172102/object-ownership-validation-in-django-updateview
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

	#http://stackoverflow.com/questions/21046626/django-form-with-a-one-to-many-relationship
	#Inlibes block
	#https://docs.djangoproject.com/en/dev/ref/contrib/admin/#inlinemodeladmin-objects

@login_required( login_url = 'client:login' )
def edit(request):
	form_project = EditProjectForm(request.POST or None)
	form_status = StatusChoiceForm(request.POST or None)
	
	if request.method == 'POST':
		if form_project.is_valid() and form_status.is_valid():
			messages.success(request, 'Datos actualizados correctamente')
	return render(request, 'project/edit.html', {'form_project' : form_project, 'form_status': form_status})

	


