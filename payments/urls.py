from . import views
from django.urls import path
urlpatterns = [
    path("create_order", views.create_order, name = "Create Order"),
    path("record_payment", views.record_payment, name = "Record Payment"),
    path("get_purchases/<int:moodleID>", views.get_purchases , name = "Get Purchases"),
]