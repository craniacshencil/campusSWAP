from django.http import JsonResponse
import os
import requests
from django.views.decorators.csrf import csrf_exempt
from .models import ProductListing, ResourceListing
import base64
import json

# Create your views here.
@csrf_exempt
def generate_image_url(request):
    if request.method == "POST":
        url = "https://api.imgbb.com/1/upload"
        # image_data = request.body
        image_data = request.body.split(b'\r\n\r\n')[1] 
        image_data = base64.b64encode(image_data)
        data = {
            "key": os.getenv('API_KEY'),
            "image": image_data,
            "expiration": 2592000,
        }
        response = requests.post(url, data)
        print(response.status_code)

        if response.status_code == 200:
            imgbb_response = response.json()
            image_url = imgbb_response['data']['url']
            return JsonResponse({'image_url': image_url}, status=200)
        else:
            print("response 200 not received")
            return JsonResponse({'error': 'Failed to upload image to ImgBB'}, status=500)
    return JsonResponse({'error': 'just an error'})

@csrf_exempt
def sell_form(request):
    if request.method == "POST":
        sell_form_data = json.loads(request.body)
        ProductListing.objects.create(
            moodleID = int(sell_form_data['moodleID']),
            title = sell_form_data['title'],
            category = sell_form_data['category'],
            price = int(sell_form_data['price']),
            selected_year = sell_form_data['selectedYear'],
            selected_branch = sell_form_data['selectedBranch'],
            selected_item_type = sell_form_data['selectedItemType'],
            selected_condition = sell_form_data['selectedCondition'],
            product_description = sell_form_data['productDesc'],
            image_urls = sell_form_data['image_urls'],
            admin_approval = sell_form_data['adminApproval'],
        )
        return JsonResponse({'message' : "Succesfully received"})
    return JsonResponse({'error' : 'No post request received'})

@csrf_exempt
def user_listings(request, moodleID):
    if request.method == "GET":
        my_listings = ProductListing.objects.filter(moodleID = moodleID).values()
        indexed_listings = {}
        for index, item in enumerate(my_listings):
            indexed_listings[index] = item
        return JsonResponse(indexed_listings)
    return JsonResponse({"error" : "Couldn't get user's listings"})

@csrf_exempt
def all_listings(request):
    if request.method == "GET":
        all_listings = ProductListing.objects.filter(admin_approval = True).values()
        indexed_listings = {}
        for index, item in enumerate(all_listings):
            indexed_listings[index] = item
        
        return JsonResponse({"allListings" : indexed_listings})
    return JsonResponse({"error" : "Couldn't get listings"})

@csrf_exempt
def upload_resource(request):
    if request.method == "POST":
        resource_json = json.loads(request.body)
        ResourceListing.objects.create(
            moodleID = int(resource_json['moodleId']),
            resource = resource_json['resource'],
        )
        return JsonResponse({'message': 'Successfully listed resource!'})
    return JsonResponse({'error': 'Post request not received'})