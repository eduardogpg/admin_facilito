#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django import forms
from django.contrib.auth.models import User
from .models import Client 
from .models import SocialNetwork

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
	username = forms.CharField( max_length = 20)
	password = forms.CharField( max_length = 20, label = 'Contraseña', widget=forms.PasswordInput())

	def __init__(self, *args, **kwargs):
		super(LoginUserForm, self).__init__(*args, **kwargs)
		self.fields['username'].widget.attrs.update({'id' : 'username_login_user', 'class': 'validate'})
		self.fields['password'].widget.attrs.update({'id' : 'password_login_user', 'class': 'validate'})

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
		self.fields['username'].widget.attrs.update({'id': 'username_create_user', 'class' : 'validate'})
		self.fields['password'].widget.attrs.update({'id': 'password_create_user', 'class' : 'validate'})
		self.fields['email'].widget.attrs.update({ 'id': 'email_create_user', 'class' : 'validate'})

	def clean_email(self):
		email = self.cleaned_data.get('email')
		if User.objects.filter(email=email).count():
			raise forms.ValidationError(u'El email debe de ser unico')
		return email

class EditUserForm(forms.ModelForm):
	username = forms.CharField( max_length = 20,  error_messages =  ERROR_MESSAGE_USER  )
	email = forms.CharField( error_messages =  ERROR_MESSAGE_EMAIL  )
	first_name = forms.CharField(label = 'Nombre completo')
	last_name = forms.CharField(label = 'Apellidos')

	class Meta:
		model = User
		fields = ('username', 'email', 'first_name', 'last_name' )

	def __init__(self, *args, **kwargs):
		super(EditUserForm, self).__init__(*args, **kwargs)
		self.fields['username'].widget.attrs.update({'id': 'username_edit_user', 'class' : 'validate'})
		self.fields['first_name'].widget.attrs.update({'id': 'first_name_edit_user', 'class' : 'validate'})
		self.fields['last_name'].widget.attrs.update({'id': 'last_name_edit_user', 'class' : 'validate'})
		self.fields['email'].widget.attrs.update({ 'id': 'email_edit_user', 'class' : 'validate'})

	def clean_email(self):
		email = self.cleaned_data.get('email')
		if User.objects.filter(email=email).exclude( pk = self.instance.id).count():
			raise forms.ValidationError(u'El email debe de ser unico')
		return email

class EditPasswordForm(forms.Form):
	password = forms.CharField( max_length = 20, widget = forms.PasswordInput() )
	new_password = forms.CharField( max_length = 20, label = "Nueva password" , widget = forms.PasswordInput(), validators = [must_be_gt] )
	repeat_password = forms.CharField( max_length = 20, label = "Repetir nueva password", widget = forms.PasswordInput(),  validators = [must_be_gt] )

	def __init__(self, *args, **kwargs):
		super(EditPasswordForm, self).__init__(*args, **kwargs)
		self.fields['password'].widget.attrs.update({'id': 'password_reset_password', 'class' : 'validate'})
		self.fields['new_password'].widget.attrs.update({'id': 'new_password_reset_password', 'class' : 'validate'})
		self.fields['repeat_password'].widget.attrs.update({'id': 'repeat_password_reset_password', 'class' : 'validate'})

	def clean(self):
		clean_data = super(EditPasswordForm,self).clean()
		password1 = clean_data.get('new_password')
		password2 = clean_data.get('repeat_password')

		if password1 != password2:
			raise forms.ValidationError('Los password no coinciden')

class EditClientForm(forms.ModelForm):

	job = forms.CharField(label= 'Trabajo actual', required = False )
	bio = forms.CharField(label= 'Biografía', required = False, widget=forms.Textarea)

	class Meta:
		model = Client
		exclude = ['user']

	def __init__(self, *args, **kwargs):
		super(EditClientForm, self).__init__(*args, **kwargs)
		self.fields['job'].widget.attrs.update({'id': 'job_edit_client', 'class' : 'validate'})
		self.fields['bio'].widget.attrs.update({'id': 'bio_edit_client', 'class' : 'validate'})

class EditClientSocial(forms.ModelForm):
	class Meta:
		model = SocialNetwork
		exclude = ['user']









