from django import forms
from .models import Status
from projects.models import Project
	
class StatusChoiceForm(forms.Form):
	status = forms.ModelChoiceField(queryset=Status.objects.all(), initial=0) 

	def __init__(self, *args, **kwargs):
		super(StatusChoiceForm, self).__init__(*args, **kwargs)
		self.fields['status'].widget.attrs.update({'class' : 'browser-default'})

	class Meta:
		model = Project
		fields = ('__all__')