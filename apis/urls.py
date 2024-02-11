from django.urls import path
from .views import save_form_data

urlpatterns = [
    path('save_form_data/', save_form_data, name='save_form_data'),
]
