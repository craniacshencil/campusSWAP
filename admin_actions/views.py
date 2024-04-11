from django.http import JsonResponse
from django.contrib.auth.models import User
from django.shortcuts import render
from products.models import ProductListing, ResourceListing
from django.views.decorators.csrf import csrf_exempt
from .models import AdminApprovalFeedback, AdminApprovalFeedbackResource
import json

# Create your views here.
def get_unapproved_listings_and_resources(request):
    if request.method == "GET":
        unapproved_listings = ProductListing.objects.filter(admin_approval= False).values()
        indexed_unapproved_listings = {}
        for index, item in enumerate(unapproved_listings):
            indexed_unapproved_listings[index] = item
        unapproved_listings_count = len(unapproved_listings) 

        unapproved_resources = ResourceListing.objects.filter(admin_approval= False).values()
        indexed_unapproved_resources = {}
        for index, item in enumerate(unapproved_resources):
            indexed_unapproved_resources[index] = item
        unapproved_resources_count = len(unapproved_resources) 

        return JsonResponse({
                'unapproved_listings': indexed_unapproved_listings,
                'unapproved_resources': indexed_unapproved_resources,
                'listings_count' : unapproved_listings_count,
                'resources_count' : unapproved_resources_count,
            })
    return JsonResponse({'error': 'No Get request received'})

@csrf_exempt
def grant_approval(request):
    if request.method == "POST":
        product_id = int(json.loads(request.body)['productId'])

        # code for when editing of a listing is allowed
        # previous_feedback = AdminApprovalFeedback.objects.get(product_id = productId)
        # if(previous_feedback):
        #     previous_feedback.delete()

        product = ProductListing.objects.get(id = product_id)
        product.admin_approval = True
        product.save()
        return JsonResponse({'Success' : "Sucessfully Registered Changes"})
    return JsonResponse({'error': 'No Post request received'})

@csrf_exempt
def send_negative_feedback(request):
    if request.method == "POST":
        feedbackJSON = json.loads(request.body)

        # code for when editing of a listing is allowed
        # previous_feedback = AdminApprovalFeedback.objects.get(product_id = feedbackJSON['productId'])
        # if(previous_feedback):
        #     previous_feedback.delete()

        AdminApprovalFeedback.objects.create(
            product_id = feedbackJSON['productId'],
            feedback = feedbackJSON['feedback'],
        )
        product = ProductListing.objects.get(id = feedbackJSON['productId'])
        product.admin_approval = 'Deny'
        product.save()
        return JsonResponse({'message': 'Sent Feedback'})
    return JsonResponse({'error': 'No Post request received'})
    
def get_negative_feedback(request, product_id):
    if request.method == "GET":
       product_feedback = AdminApprovalFeedback.objects.get(product_id = product_id)
       return JsonResponse({
           'feedback': product_feedback.feedback,
       })
    return JsonResponse({'error': 'No Get request received'})

@csrf_exempt
def grant_approval_resource(request):
    if request.method == "POST":
        resource_id = int(json.loads(request.body)['resourceId'])

        # code for when editing of a listing is allowed
        # previous_feedback = AdminApprovalFeedback.objects.get(product_id = productId)
        # if(previous_feedback):
        #     previous_feedback.delete()

        resource = ResourceListing.objects.get(id = resource_id)
        resource.admin_approval = True
        resource.save()
        return JsonResponse({'Success' : "Sucessfully Registered Changes"})
    return JsonResponse({'error': 'No Post request received'})

@csrf_exempt
def send_negative_feedback_resource(request):
    if request.method == "POST":
        feedbackJSON = json.loads(request.body)
        print(feedbackJSON)
        # code for when editing of a listing is allowed
        # previous_feedback = AdminApprovalFeedback.objects.get(product_id = feedbackJSON['productId'])
        # if(previous_feedback):
        #     previous_feedback.delete()

        AdminApprovalFeedbackResource.objects.create(
            resource_id = feedbackJSON['resourceId'],
            feedback = feedbackJSON['feedback'],
        )
        print(feedbackJSON)
        resource = ResourceListing.objects.get(id = feedbackJSON['resourceId'])
        resource.admin_approval = 'Deny'
        resource.save()
        return JsonResponse({'message': 'Sent Feedback'})
    return JsonResponse({'error': 'No Post request received'})
    
def get_negative_feedback_resource(request, resource_id):
    if request.method == "GET":
       resource_feedback = AdminApprovalFeedbackResource.objects.get(resource_id = resource_id)
       return JsonResponse({
           'feedback': resource_feedback.feedback,
       })
    return JsonResponse({'error': 'No Get request received'})

def get_all_users(request):
    if request.method == "GET":
        users = User.objects.filter(is_superuser = False)
        all_users = []
        for user in users:
            info = {
               "username": user.username,
               "first_name": user.first_name,
               "last_name": user.last_name,
            }
            all_users.append(info)
        return JsonResponse({'all_users':all_users})
    return JsonResponse({"error" : "There was an error fetching all the users"})
