from . import views
from django.urls import path
urlpatterns = [
    path("create_order", views.create_order, name = "Create Order"),
]