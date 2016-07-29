from django.shortcuts import render
from django.contrib.auth.models import User
from django.shortcuts import redirect

def home(request):
	if request.user.is_authenticated():
		return redirect('client:dashboard')
	return render(request, 'home.html', {})

def error_404(request):
	return render(request, 'error_404.html', {})	