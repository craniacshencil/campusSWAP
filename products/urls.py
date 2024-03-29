from . import views
from django.urls import path
urlpatterns = [
    path("image_url_gen", views.generate_image_url, name = "image_url_gen"),
    path("sell_form", views.sell_form, name = "sell_form"),
    path("user_listings/<int:moodleID>", views.user_listings, name = "user_listings"),
    path("all_listings", views.all_listings, name = "all_listings"),
    path("upload_resource", views.upload_resource, name = "upload_resource")
] 