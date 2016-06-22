from django.shortcuts import render
from django.shortcuts import redirect

from django.http import HttpResponse

from django.contrib.auth.models import User

from django.contrib.auth import authenticate
from django.contrib.auth import login as login_django
from django.contrib.auth import logout as logout_django

from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test

from forms import LoginForm
from forms import CreateUserForm

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from django.views.generic import View,DetailView

#decoradores
def user_authenticated(user):
	return not user.is_authenticated()

# Create your views here.
def show_(request):
	return HttpResponse("Hola Mundo desde el cliente")

#https://docs.djangoproject.com/en/dev/topics/class-based-views/generic-display/#dynamic-filtering
#http://stackoverflow.com/questions/19407239/generic-detail-view-must-be-called-with-either-an-object-pk-or-a-slug
#http://stackoverflow.com/questions/31947764/passing-pk-or-slug-to-generic-detailview-in-django
#El de arriba
class Ver(DetailView):
	model = User
	template_name = 'show.html'
	slug_field = 'username'
	slug_url_kwarg = 'username_slug'


class Show(TemplateView):
	template_name = "show.html"

class Login(View):
	form = LoginForm()
	message = None
	template = 'login.html'

	def get(self, request, *args, **kwargs):
		if request.user.is_authenticated():
			return redirect('client:dashboard')
		return render( request, self.template,  self.get_context() )

	def post(self, request, *args, **kwargs):
		username_post = request.POST['username']
		password_post = request.POST['password']
		user = authenticate( username = username_post, password = password_post)
		print "\n\n\n\n\n\n"
		print type(user)#objecto models
		if user is not None:
			login_django(request, user)
			return redirect('client:dashboard')
		else:
			self.message = 'Username o password incorrectos'

		return render( request, 'login.html', self.get_context() )	

	def get_context(self):
		return { 'form': self.form, 'message' : self.message }


@user_passes_test(user_authenticated, login_url = 'client:dashboard')
def login_dos(request):
	message = None
	if request.method == 'POST':#se envio el formulario
		username_post = request.POST['username']
		password_post = request.POST['password']
		user = authenticate( username = username_post, password = password_post)
		if user is not None:
			login_django(request, user)
			return redirect('client:dashboard')
		else:
			message = 'Username o password incorrectos'

	form = LoginForm()
	context = {
		'form' : form,
		'message' : message
	}
	return render( request, 'login.html', context )

@login_required(login_url = 'client:login')
def dashboard(request):
	username = request.user.username
	return render( request, 'dashboard.html', {'username' : username} )	

def logout(request):
	logout_django(request)
	return redirect('client:login')

#nuevo feature
class Dashboard(LoginRequiredMixin, View):
    login_url = 'client:login'
    
    def get(self, request, *args, **kwargs):
    	return render( request, 'dashboard.html', {} )	

def create(request):
	message = None
	form = CreateUserForm(request.POST or None)
	if request.method =='POST':
		if form.is_valid():
			user = form.save( commit = False )
			password = user.password #Este en texto plano
			user.set_password(password)
			user.save()
			return redirect('client:login')
		else:
			message = "Formulario no valido"

	context = {
		'form':  form,
		'message' : message
	}
	return render( request, 'create.html', context )









