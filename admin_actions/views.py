from django.http import JsonResponse
from django.shortcuts import render
from products.models import Prouduct_listing 

# Create your views here.
def get_unapproved_listings_and_resources(request):
    if request.method == "GET":
        products = Prouduct_listing.objects.filter(admin_approval = 'false').values()
        unapproved_listings = len(products) 
        unapproved_resources = 0
        return JsonResponse({
                'listings' : unapproved_listings,
                'resources' : unapproved_resources,
            })
    return JsonResponse({'error': 'No Get request received'})

