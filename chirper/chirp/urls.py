"""
URL configuration for chirper project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.chirp_list, name='chirp_list'),
    path('create/', views.chirp_create, name='chirp_create'),
    path('edit/<int:chirp_id>', views.chirp_edit, name='chirp_edit'),
    path('delete/<int:chirp_id>', views.chirp_delete, name='chirp_delete'),
    path('register', views.register, name='register'),
] 
