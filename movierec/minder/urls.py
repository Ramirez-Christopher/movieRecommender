from django.urls import path
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView

from .views import SignUpView

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("popular_movies/", views.popular_movies, name="popular_movies"),
    path("signup/", SignUpView.as_view(), name="signup"),
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),

]