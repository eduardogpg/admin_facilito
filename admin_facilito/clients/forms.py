from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm

"""
module_name, package_name, ClassName, 
method_name, 
ExceptionName, function_name, GLOBAL_CONSTANT_NAME, 
global_var_name, 
instance_var_name, 
function_parameter_name, 
local_var_name
"""

"""
Constants
"""
error_messages_user =  {	'required' : 'El username es requerido', 'unique' : 'El username ya se encuentra registrado', 'invalid': 'El username es incorrecto', 'min_length': "El username debe de ser de por lo menos 2 caracteres"}
error_messages_password = {'required' : 'El password es requerido'}
error_messages_email = {'required' : 'El email es requerido', 'invalid': 'Ingrese un correo valido'} 

"""
Functions
"""

def must_be_gt(value):
	if len(value) <= 2:
		raise forms.ValidationError("El valor debe de ser mayor a 2")

"""
Class
"""
 

class LoginForm(forms.Form):
	username = forms.CharField( max_length = 20)
	password = forms.CharField( max_length = 20, widget = forms.PasswordInput() )

class CreateUserForm(forms.ModelForm):
	username = forms.CharField( max_length = 20, min_length = 2, error_messages =  error_messages_user )

	password = forms.CharField( max_length = 20, widget = forms.PasswordInput() ,
															error_messages =  error_messages_password , validators = [must_be_gt]  )

	email = forms.CharField( error_messages =  error_messages_email )

	class Meta:
		model = User
		fields = ('username', 'password', 'email')

	def clean_email(self):
		email = self.cleaned_data['email']
		if not email.lower().endswith(".com"):
			raise forms.ValidationError("Nop :P ")
		return email

class EditUserForm(forms.ModelForm):
	username = forms.CharField( max_length = 20, error_messages =  error_messages_user )

	password = forms.CharField( max_length = 20, widget = forms.PasswordInput() ,
															error_messages =  error_messages_password  )

	class Meta:
		model= User
		fields = ('username','first_name', 'last_name', 'email')
