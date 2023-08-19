from django.urls import path

from . import views

app_name = 'todo'

urlpatterns = [
    path('', views.index, name='index'),
    path('update/<str:pk>/', views.update, name='update'),
    path('delete/<str:pk>/', views.delete, name='delete'),
]