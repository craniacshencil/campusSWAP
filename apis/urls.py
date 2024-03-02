from . import views
from django.urls import path
urlpatterns = [
    path("register", views.register, name = "register"),
    path("login", views.login_page, name = "login"),
]