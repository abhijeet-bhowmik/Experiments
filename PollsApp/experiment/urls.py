from django.urls import path, include
from django.views.generic.base import TemplateView
from . import views


urlpatterns = [
	path('', include('django.contrib.auth.urls')),
    path('users/', views.getusers , name='users'),
    path('register/', views.register, name = 'register'),
    path('base/', views.baseView, name='baseView')
]