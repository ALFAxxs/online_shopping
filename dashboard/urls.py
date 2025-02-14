from django.urls import path

from . import views

app_name = 'dashboard'

urlpatterns = [
    # path('<str:user_name>/', views.index, name='dashboard'),
    path('dashboard/', views.index, name='dashboard'),
]