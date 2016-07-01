from django.shortcuts import render


"""
Debemos de crear una carpeta template
dentro de settings agregamos el directiorio, templates
"""

def home(request):
	return render(request, 'home.html', {})
