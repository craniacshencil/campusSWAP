from . import views
from django.urls import path
urlpatterns = [
    path("register", views.register, name = "register"),
    path("login", views.login_page, name = "login"),
    path("logout", views.logout_page, name = "logout"),
    path("reset_password", views.reset_password, name = "reset_password"),
]