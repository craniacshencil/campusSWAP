from django.http import JsonResponse
from django.shortcuts import render
from products.models import Prouduct_listing 
from django.views.decorators.csrf import csrf_exempt
from .models import AdminApprovalFeedback
import json

# Create your views here.
def get_unapproved_listings_and_resources(request):
    if request.method == "GET":
        unapproved_listings = Prouduct_listing.objects.filter(admin_approval= False).values()
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

@csrf_exempt
def grant_approval(request):
    if request.method == "POST":
        product_id = int(json.loads(request.body)['productId'])
        # print(f"Product id: {product_id} {type(product_id)}")
        product = Prouduct_listing.objects.get(id = product_id)
        product.admin_approval = True
        product.save()
        return JsonResponse({'Success' : "Sucessfully Registered Changes"})
    return JsonResponse({'error': 'No Post request received'})

@csrf_exempt
def send_negative_feedback(request):
    if request.method == "POST":
        feedbackJSON = json.loads(request.body)
        AdminApprovalFeedback.objects.create(
            product_id = feedbackJSON['productId'],
            feedback = feedbackJSON['feedback'],
        )
        return JsonResponse({'message': 'Sent Feedback'})
    return JsonResponse({'error': 'No Post request received'})
    

