from . import views
from django.urls import path
urlpatterns = [
    path("get_unapproved_listings_and_resources", views.get_unapproved_listings_and_resources, name = "unapproved listings and resources"),
]