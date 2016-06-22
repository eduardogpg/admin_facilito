from django.shortcuts import render
from django.shortcuts import redirect

from django.http import HttpResponse

from django.contrib.auth import authenticate
from django.contrib.auth import login as login_django
from django.contrib.auth import logout as logout_django

from django.contrib.auth.decorators import login_required

from forms import LoginForm
from forms import CreateUserForm

def show(request):
	return HttpResponse("Hola Mundo desde el cliente")

def login(request):
 	if request.user.is_authenticated():
		return redirect('client:dashboard')

	message = None

	if request.method == 'POST':#No estan enviando el formulario
		username_post = request.POST['username']
		password_post = request.POST['password']
		user = authenticate( username = username_post , password = password_post)
		if user is not None:
			login_django( request, user)
			return redirect('client:dashboard')
		else:
			message = "Username o password incorrectos"
		
	form = LoginForm()
	context = {
		'form' : form,
		'message' : message
	}
	return render( request, 'login.html', context)

@login_required( login_url = 'client:login' )
def dashboard(request):
	return render( request, 'dashboard.html', {})


@login_required( login_url = 'client:login' )
def logout(request):
	logout_django(request)
	return redirect('client:login')


def create(request):
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













