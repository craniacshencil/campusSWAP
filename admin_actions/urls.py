from . import views
from django.urls import path
urlpatterns = [
    path("get_unapproved_listings_and_resources", views.get_unapproved_listings_and_resources, name = "Get unapproved listings and resources"),
    path("grant_approval", views.grant_approval, name = "Grant Approval"),
    path("send_negative_feedback", views.send_negative_feedback, name = "Send negative feedback"),
    path("get_negative_feedback/<int:product_id>", views.get_negative_feedback, name = "Get negative feedback"),
]