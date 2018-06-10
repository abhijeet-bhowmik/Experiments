from django.shortcuts import render, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User

from . import models

# Create your views here.


def register(request):
	if request.method=='POST':
		f = models.CustomUserCreationForm(request.POST)
		if f.is_valid():
			f.save()
			messages.success(request, "Registration Successful")
			return HttpResponseRedirect(reverse('login'))
		else:
			print("error.......")
	else:
			f =models. CustomUserCreationForm()
	return render(request, 'registration/register.html', {'form' : f})

def getusers(request):
	users = User.objects.all()
	content = {'users' : users}
	return render(request, 'users.html', content)

def baseView(request):
	return render(request, 'base.html', {})
