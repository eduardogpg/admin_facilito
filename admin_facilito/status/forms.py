from django import forms
from .models import Status
from projects.models import Project
	
class StatusChoiceForm(forms.Form):
	status = forms.ModelChoiceField(queryset=Status.objects.all(), initial=0) 

	class Meta:
		model = Project
		fields = ('__all__')
	
