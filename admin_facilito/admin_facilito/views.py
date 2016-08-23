from django.shortcuts import render
from django.contrib.auth.models import User
from django.shortcuts import redirect

from projects.models import Project

def home(request):
	if request.user.is_authenticated():
		return redirect('client:dashboard')

	projects = [] #Project.objects.all()[:5]
	return render(request, 'home.html', {'projects' : projects})

def error_404(request):
	return render(request, 'error_404.html', {})	