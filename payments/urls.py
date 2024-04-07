from . import views
from django.urls import path
urlpatterns = [
    path("create_order", views.create_order, name = "Create Order"),
    path("record_payment", views.record_payment, name = "Record Payment"),
]