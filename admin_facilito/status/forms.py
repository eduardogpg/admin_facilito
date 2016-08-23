from django import forms
from .models import Status

class StatusChoiceForm(forms.Form):
	status = forms.ModelChoiceField(queryset=Status.objects.order_by('id'))
