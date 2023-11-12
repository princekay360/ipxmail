from django.urls import path
from . import views

urlpatterns = [
    path('mozamas', views.index, name='mozamas_index'),
    path('mozamas/login', views.login, name='m_login'),
]