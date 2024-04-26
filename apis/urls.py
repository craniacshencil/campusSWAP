from . import views
from django.urls import path
urlpatterns = [
    path("register", views.register, name = "Register"),
    path("login", views.login_page, name = "Login"),
    path("logout", views.logout_page, name = "Logout"),
    path("reset_password", views.reset_password, name = "Reset Password"),
    path("get_phone/<int:moodleID>", views.get_phone , name = "Get phonenumber"),
]