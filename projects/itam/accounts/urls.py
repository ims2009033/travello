from django.urls import path

from . import views 

urlpatterns = [
    path("register", views.register, name='register'),
    path("submit", views.submit, name='submit'),
    path("asset_list", views.asset_list, name='asset_list'),
    path("asset_register", views.asset_register, name='asset_register'),
    path("login", views.login, name='login'),
    path("logout", views.logout, name='logout')
]