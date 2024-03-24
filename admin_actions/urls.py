from . import views
from django.urls import path
urlpatterns = [
    path("get_unapproved_listings_and_resources", views.get_unapproved_listings_and_resources, name = "Get unapproved listings and resources"),
]