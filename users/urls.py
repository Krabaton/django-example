from django.conf.urls import url
from django.urls import path
from django.contrib.auth.views import LoginView
from . import views

urlpatterns = [
    # Home page
    url(r'^login/$', LoginView.as_view(template_name='users/login.html'), name='login'),
    url('logout/', views.logout_view, name='logout'),
    url('register/', views.register, name='register'),
]
