from django.urls import path
from . import views

app_name = 'item'

urlpatterns = [
    path('', views.items, name='items'),
    path('<int:pk>/', views.detail, name='detail'),
    path('new/', views.NewItemView, name='new'),
    path('<int:pk>/delete/', views.DeletItemsView, name='delete'),
    path('<int:pk>/edit/', views.EditItemView, name='edit')
]