from django.shortcuts import render
from django.http import HttpResponse

def show(request):
	return HttpResponse("Hola Mundo desde el cliente")

def login(request):
	return render( request, 'login.html', {})
