#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django import forms
from django.contrib.auth.models import User
from .models import Client 

"""
Constants
"""
ERROR_MESSAGE_USER = {'required' : 'El username es requerido', 'unique' : 'El username ya se encuentra registrado', 'invalid': 'El username es incorrecto' }
ERROR_MESSAGE_PASSWORD = {'required' : 'El password es requerido'} 
ERROR_MESSAGE_EMAIL = {'required' : 'El email es requerido', 'invalid': 'Ingrese un correo valido'}


"""
Functions
"""
def must_be_gt(value_password):
	if len(value_password) < 2:
		raise forms.ValidationError('El password debe contener por lo menos 5 caracteres.')

"""
Class
"""

class LoginUserForm(forms.Form):
	username = forms.CharField( max_length = 20, 
															widget=forms.TextInput(attrs={'id': 'login_username', 'class': 'validate' }))

	password = forms.CharField( max_length = 20, label = 'Contraseña', 
															widget = forms.PasswordInput(attrs={'id': 'login_password', 'class': 'validate' }) )

class CreateUserForm(forms.ModelForm):
	error_css_class = 'error_input'
	required_css_class = 'required_input'

	username = forms.CharField( max_length = 20,  error_messages =  ERROR_MESSAGE_USER  )
	password = forms.CharField( max_length = 20, widget = forms.PasswordInput(), error_messages =  ERROR_MESSAGE_PASSWORD, label = 'Contraseña'  )
	email = forms.CharField( error_messages =  ERROR_MESSAGE_EMAIL )

	class Meta:
		model = User
		fields = ('username', 'password', 'email')

	def __init__(self, *args, **kwargs):
		super(CreateUserForm, self).__init__(*args, **kwargs)
		self.fields['username'].widget.attrs.update({'class' : 'create_use_form'})
		self.fields['password'].widget.attrs.update({'class' : 'password_use_form'})
		self.fields['email'].widget.attrs.update({'class' : 'email_use_form'})

class EditUserForm(forms.ModelForm):
	username = forms.CharField( max_length = 20,  error_messages =  ERROR_MESSAGE_USER  )
	email = forms.CharField( error_messages =  ERROR_MESSAGE_EMAIL  )
	first_name = forms.CharField(label = 'Nombre completo')
	last_name = forms.CharField(label = 'Apellidos')


	class Meta:
		model = User
		fields = ('username', 'email', 'first_name', 'last_name' )

class EditPasswordForm(forms.Form):
	password = forms.CharField( max_length = 20, widget = forms.PasswordInput() )
	new_password = forms.CharField( max_length = 20, label = "Nueva password" , widget = forms.PasswordInput(), validators = [must_be_gt] )
	repeat_password = forms.CharField( max_length = 20, label = "Repetir nueva password", widget = forms.PasswordInput(),  validators = [must_be_gt] )


	def clean(self):
		clean_data = super(EditPasswordForm,self).clean()
		password1 = clean_data.get('new_password')
		password2 = clean_data.get('repeat_password')

		if password1 != password2:
			raise forms.ValidationError('Los password no coinciden')

class EditClientForm(forms.ModelForm):

	class Meta:
		model = Client
		exclude = ['user']










