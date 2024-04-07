from django.urls import path

from . import views

urlpatterns = [
    path('login', views.login),
    path('client/register', views.postClient),
    path('agent/register', views.postAgent),
]