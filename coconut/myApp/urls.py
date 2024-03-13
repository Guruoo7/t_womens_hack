from . import views
from django.urls import path

urlpatterns = [
    path("", views.home, name="home"),
    path("login.html", views.login, name="login"),
    path("login/", views.login, name="login"),
    path("login/course.html", views.course, name="course"),
    path('register.html', views.register, name="register"),
    path('register/', views.register, name='register'), 
    path('register/login/', views.login, name='register_login'), 
]