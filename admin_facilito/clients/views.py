from django.shortcuts import render
from django.http import HttpResponse
from .forms import Login

# Create your views here.
def show(request):
	return HttpResponse("Hola Mundo desde el cliente")

def login(request):
	form = Login()
	contex = {
		'form' : form
	}
	return render( request, 'login.html', contex  )