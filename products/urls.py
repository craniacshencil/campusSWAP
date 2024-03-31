from . import views
from django.urls import path
urlpatterns = [
    path("image_url_gen", views.generate_image_url, name = "image_url_gen"),
    path("sell_form", views.sell_form, name = "sell_form"),
    path("get_resource/<int:resourceId>", views.get_resource, name = "Get Resource"),
    path("user_listings_and_resources/<int:moodleID>", views.user_listings_and_resources, name = "user_listings_and_resources"),
    path("all_approved_listings", views.all_approved_listings, name = "all_approved_listings"),
    path("upload_resource", views.upload_resource, name = "upload_resource")
] 