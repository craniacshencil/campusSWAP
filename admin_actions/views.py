from django.http import JsonResponse
from django.shortcuts import render
from products.models import Prouduct_listing 

# Create your views here.
def get_unapproved_listings_and_resources(request):
    if request.method == "GET":
        unapproved_listings = Prouduct_listing.objects.filter(admin_approval = 'false').values()
        indexed_unapproved_listings = {}
        for index, item in enumerate(unapproved_listings):
            indexed_unapproved_listings[index] = item
        unapproved_listings_count = len(unapproved_listings) 

        unapproved_resources_count = 0 #edit later 
        return JsonResponse({
                'listings': indexed_unapproved_listings,
                'listings_count' : unapproved_listings_count,
                'resources_count' : unapproved_resources_count,
            })
    return JsonResponse({'error': 'No Get request received'})

