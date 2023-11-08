from django.urls import path
from . import views

urlpatterns = [
    path("", views.landing, name="landing"),
    path("login/", views.login_view, name="login"),
    path("register/", views.register, name="register"),
    path("complete-register/", views.complete_register, name="complete-register"),
    path("about/", views.about, name="about"),
    path('logout/', views.logout, name='logout'),
]