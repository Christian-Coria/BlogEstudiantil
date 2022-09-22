from django.contrib.auth import views as auth_views
from django.urls import path

from chat import views

urlpatterns = [
    path('frontchat', views.frontchat, name='frontchat'),
    path('signup/', views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='core/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]