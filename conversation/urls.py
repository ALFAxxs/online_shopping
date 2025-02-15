from django.urls import path

from . import views

app_name = 'conversation'

urlpatterns = [
    path('', views.Inbox, name='inbox'),
    path('<int:pk>/', views.detail, name='detail'),
    path('new/<int:item_pk>/', views.NewConversationView, name='new')
]