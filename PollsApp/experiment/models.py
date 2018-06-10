from django.db import models
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

# Create your models here.


class CustomUserCreationForm(forms.Form):
	first_name = forms.CharField(label='First Name')
	last_name = forms.CharField(label='Last Name')
	username = forms.CharField(label='Username', min_length=4, max_length=12)
	email = forms.EmailField(label='Email ID')
	password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
	password2 = forms.CharField(label='Confirm your password', widget=forms.PasswordInput)


	def clean_username(self):
		username = self.cleaned_data['username'].lower()
		usr = User.objects.filter(username=username)
		if usr.count():
			raise ValidationError('User already exist')
		return username

	def clean_email(self):
		email = self.cleaned_data['email'].lower()
		usr = User.objects.filter(email=email)
		if usr.count():
			raise ValidationError('Email already registered.')
		return email

	def clean_password(self):
		password1 = self.cleaned_data.get('password1')
		password2 = self.cleaned_Data.get('password2')
		if password1 and password2 and password1 != password2:
			raise ValidationError('Enter the same password')
		return password1

	def save(self, commit=True):
		user= User.objects.create_user(self.cleaned_data['username'], self.cleaned_data['email'], self.cleaned_data['password1'])
		#user.first_name = self.first_name
		#user.last_name = self.last_name
		return user




