from django.contrib.auth.models import User
from .models import Client
from .models import SocialNetwork

from django.shortcuts import render
from django.shortcuts import redirect

from django.contrib.auth.models import User

from django.contrib.auth import authenticate
from django.contrib.auth import login as login_django
from django.contrib.auth import logout as logout_django
from django.contrib.auth import update_session_auth_hash

from django.contrib.auth.decorators import login_required

from forms import LoginUserForm
from forms import CreateUserForm
from forms import EditUserForm
from forms import EditPasswordForm
from forms import EditClientForm
from forms import EditClientSocial

from django.views.generic import TemplateView
from django.views.generic import View
from django.views.generic import DetailView
from django.views.generic import CreateView
from django.views.generic.edit import UpdateView
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

from django.contrib.auth.mixins import LoginRequiredMixin

from django.core.urlresolvers import reverse_lazy
from django.core.mail import send_mail

from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin

from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.http import HttpResponseRedirect

import json

"""
Class
"""

class ShowClass(DetailView):
	model = User
	template_name = 'client/show.html'
	slug_field = 'username'
	slug_url_kwarg = 'username_url'

class LoginClass(View, SuccessMessageMixin):
	form = LoginUserForm()
	error_message = 'El username o password incorrectos'
	template = 'client/login.html'

	def get(self, request, *args, **kwargs):
		if request.user.is_authenticated():
			return redirect('client:dashboard')
		return render(request, self.template, self.get_context() )

	def post(self, request, *args, **kwargs):
		username_post = request.POST['username']
		password_post = request.POST['password']
		user = authenticate( username = username_post , password = password_post)
		if user is not None:
			login_django( request, user)
			return redirect('client:dashboard')
		else:
			messages.success(self.request, self.error_message)
		return render(request, self.template, self.get_context() )

	def get_context(self):
		return {'form': self.form }

class DashboardClass(LoginRequiredMixin, View):
	login_url = 'client:login'
	def get(self, request, *args, **kwargs):
		return render( request, 'client/dashboard.html', {})

class CreateClass(CreateView):
	success_url =  reverse_lazy('client:login')
	template_name = 'client/create.html'
	model = User
	form_class = CreateUserForm

	def form_valid(self, form):
		self.object = form.save(commit = False)
		self.object.set_password ( self.object.password)
		self.object.save()
		return HttpResponseRedirect( self.get_success_url() ) 

class EditSocialClass(LoginRequiredMixin, UpdateView,SuccessMessageMixin):
	login_url = 'client:login'
	model = SocialNetwork
	template_name = 'client/edit_social.html'
	success_url = reverse_lazy('client:edit_social_n')
	form_class = EditClientSocial
	success_message = "Tu usuarios ha sido actualizado exitosamente."

	def get_object(self, queryset = None):
		""" By default this requires `self.queryset` and a `pk` or `slug` argument """
		return self.get_social_instance()

	def get_social_instance(self):
		try:
			return self.request.user.socialnetwork
		except:
			return SocialNetwork(user = self.request.user)

"""
Functions
"""
@login_required( login_url = 'client:login' )
def edit_password(request):
	form = EditPasswordForm(request.POST or None)
	if request.method == 'POST':
		if form.is_valid():
			current_password = form.cleaned_data['password']
			new_password = form.cleaned_data['new_password']

			if authenticate(username = request.user.username, password = current_password):
				request.user.set_password(  new_password )
				request.user.save()

				update_session_auth_hash( request, request.user )
				messages.success(request, 'El password ha sido actualizado')
			else:
				messages.error(request, 'El password no es el correcta')

	context = {'form' : form}
	return render(request, 'client/edit_password.html', context)

@login_required( login_url = 'client:login' )
def logout(request):
	logout_django(request)
	return redirect('client:login')

@login_required( login_url = 'client:login' )
def edit_client(request):
	form_client = EditClientForm(request.POST or None, instance = client_instance(request.user) )
	form_user = EditUserForm(request.POST or None, instance= request.user)

	if request.method == 'POST':
		if form_client.is_valid() and form_user.is_valid():
			form_user.save()
			form_client.save()	
			messages.success(request, 'Datos actualizados correctamente')
	return render(request, 'client/edit.html', {'form_client' : form_client, 'form_user': form_user})

def reset_password(request):
	return render(request,'client/reset_password.html',{})

@csrf_exempt
@require_http_methods(["POST"])
def search(request):
	val_user = request.POST.get('user')
	users = User.objects.filter(username__startswith=val_user).order_by('username').values('id', 'username')
	data = json.dumps(list(users))
	
	return HttpResponse(
		data,
		content_type="application/json"
	)

def client_instance(user):
	try:
		return user.client
	except:
		return Client(user = user)


	
