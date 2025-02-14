from django.urls import path
from django.contrib.auth import views as auth_view

from . import forms
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
    path('signup/', views.SignupView, name='signup'),
    path('logout/', views.logout_view, name='logout'),
    path('login/', auth_view.LoginView.as_view(template_name='login.html', authentication_form=forms.AuthenticationForm), name='login')
]