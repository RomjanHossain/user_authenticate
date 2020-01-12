from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('sign_up/', views.sign_up, name='signup'),
    path('index/', views.index, name='index'),
]
