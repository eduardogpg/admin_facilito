from django.contrib.auth.models import User

from django.shortcuts import render
from django.shortcuts import redirect

from django.contrib.auth.models import User

from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth import logout

from django.contrib.auth.decorators import login_required

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from django.views.generic import View
from django.views.generic import DetailView
from django.views.generic import CreateView
from django.views.generic import DeleteView
from django.views.generic.edit import UpdateView

from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponseRedirect

from forms import LoginForm
from forms import CreateUserForm
from forms import EditUserForm

class ShowClass(DetailView):
	model = User
	template_name = 'show.html'
	slug_field = 'username'
	slug_url_kwarg = 'username_url'

class ShowUser(TemplateView):
	template_name = "show.html"

class LoginClass(View):
	form = LoginForm()
	message = None
	template = 'login.html'

	def get(self, request, *args, **kwargs):
		if request.user.is_authenticated():
			return redirect('client:dashboard')
		return render(request, self.template, self.get_context() )

	def post(self, request, *args, **kwargs):
		username_post = request.POST['username']
		password_post = request.POST['password']
		user = authenticate( username = username_post , password = password_post)
		if user is not None:
			login( request, user)
			return redirect('client:dashboard')
		else:
			self.message = "Username o password incorrectos"
		return render(request, self.template, self.get_context() )

	def get_context(self):
		return {'form': self.form, 'message' : self.message}

class DashboardClass(LoginRequiredMixin, View):
	login_url = 'client:login'
	def get(self, request, *args, **kwargs):
		return render( request, 'dashboard.html', {})


@login_required(login_url = 'client:login' )
def logout_function(request):
	logout(request)
	return redirect('client:login')

class CreateClass(CreateView):
	template_name = "create.html"
	success_url = reverse_lazy("client:login")
	form_class = CreateUserForm
	model = User
	
	# This method is called when valid form data has been POSTed.
	# It should return an HttpResponse.
	def form_valid(self, form):
		self.object = form.save(commit=False)
		self.object.set_password(self.object.password)
		self.object.save()
		return HttpResponseRedirect(self.get_success_url())

class DeleteClass(LoginRequiredMixin, DeleteView):
		login_url = 'client:login'
		template_name = "delete.html"
		slug_field = 'username'
		slug_url_kwarg = 'username_url'
	 	model = User
		success_url = reverse_lazy("client:login")

#http://stackoverflow.com/questions/15497693/django-can-class-based-views-accept-two-forms-at-a-time
class _Update(UpdateView):
	model = User
	form_class = EditUserForm
	template_name_suffix = 'update.html'
	template_name = "update.html"
	slug_field = 'username'
	slug_url_kwarg = 'username_url'
	success_url = reverse_lazy("client:edit", kwargs={'username_url': 'eduardo'})

class UpdateClass(UpdateView):
	form_class = EditUserForm
	template_name = "update.html"
	success_url = reverse_lazy("client:edit")

	#get object
	def get_object(self, queryset=None): 
		return self.request.user

def creates(request):
	#queryset = Poll.active.order_by('-pub_date')[:5]
	message = None
	form = CreateUserForm(request.POST or None)
	if request.method == 'POST':
		if form.is_valid():
			user = form.save( commit = False )
			user.set_password( user.password )
			user.save()
			return redirect('client:login')
	context = {
		'form' : form
	}
	return render( request, 'create.html', context)













