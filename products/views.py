from django.http import JsonResponse
import os
import requests
from django.views.decorators.csrf import csrf_exempt
from .models import ProductListing, ResourceListing, StarredResources
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
def upload_listing(request):
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
            admin_approval = False,
        )
        return JsonResponse({'message' : "Succesfully received"})
    return JsonResponse({'error' : 'No post request received'})

@csrf_exempt
def update_listing(request):
    if request.method == "POST":
        listing_json = json.loads(request.body)
        listing_to_be_updated = ProductListing.objects.get(id = listing_json['id'])
        listing_to_be_updated.title = listing_json['title']
        listing_to_be_updated.category = listing_json['category']
        listing_to_be_updated.price = listing_json['price']
        listing_to_be_updated.product_description = listing_json['productDesc']
        listing_to_be_updated.selected_year = listing_json['selectedYear']
        listing_to_be_updated.selected_branch = listing_json['selectedBranch']
        listing_to_be_updated.selected_item_type = listing_json['selectedItemType']
        listing_to_be_updated.selected_condition = listing_json['selectedCondition']
        listing_to_be_updated.image_urls= listing_json['image_urls']
        listing_to_be_updated.admin_approval = False
        listing_to_be_updated.save()
        return JsonResponse({'message' : "Succesfully updated"})
    return JsonResponse({'error' : 'No post request received'})



def get_resource(request, resourceId):
    if request.method == "GET":
        resourceEntry = ResourceListing.objects.get(id = resourceId)
        return JsonResponse({
            "id": resourceEntry.id,
            "admin_approval": resourceEntry.admin_approval,
            "resource": resourceEntry.resource,
            "moodleID": resourceEntry.moodleID,
            "stars": resourceEntry.stars,
        })
    return JsonResponse({'error' : 'No post request received'})

@csrf_exempt
def user_listings_and_resources(request, moodleID):
    if request.method == "GET":

        my_listings = ProductListing.objects.filter(moodleID = moodleID).values()
        indexed_listings = {}
        for index, item in enumerate(my_listings):
            indexed_listings[index] = item

        my_resources = ResourceListing.objects.filter(moodleID = moodleID).values()
        indexed_resources = {}
        for index, item in enumerate(my_resources):
            indexed_resources[index] = item

        return JsonResponse({
            'listings' : indexed_listings, 
            'resources': indexed_resources
        })
    return JsonResponse({"error" : "Couldn't get user's listings"})

@csrf_exempt
def all_approved_listings(request):
    if request.method == "GET":
        all_listings = ProductListing.objects.filter(admin_approval = True).values()
        indexed_listings = {}
        for index, item in enumerate(all_listings):
            indexed_listings[index] = item
        
        return JsonResponse({"allApprovedListings" : indexed_listings})
    return JsonResponse({"error" : "Couldn't get listings"})

@csrf_exempt
def all_approved_resources(request):
    if request.method == "GET":
        all_resources = ResourceListing.objects.filter(admin_approval = True).values()
        indexed_resources = {}
        for index, item in enumerate(all_resources):
            indexed_resources[index] = item

        return JsonResponse({"allApprovedResources" : indexed_resources})
    return JsonResponse({"error" : "Couldn't get resources"})

@csrf_exempt
def upload_resource(request):
    if request.method == "POST":
        resource_json = json.loads(request.body)
        ResourceListing.objects.create(
            moodleID = int(resource_json['moodleId']),
            resource = resource_json['resource'],
            admin_approval = False,
        )
        return JsonResponse({'message': 'Successfully listed resource!'})
    return JsonResponse({'error': 'Post request not received'})

@csrf_exempt
def update_resource(request):
    if request.method == "POST":
        resource_json = json.loads(request.body)
        resource_to_be_updated = ResourceListing.objects.get(id = resource_json['id'])
        resource_to_be_updated.admin_approval = False
        resource_to_be_updated.resource = resource_json['resource']
        resource_to_be_updated.save()
        return JsonResponse({'message': 'Successfully updated resource!'})
    return JsonResponse({'error': 'Post request not received'})

@csrf_exempt
def user_starred_resources(request, moodleID):
    if request.method == "GET":
        starred_resources_ids = StarredResources.objects.filter(moodleID = moodleID).values_list('resourceID')
        starred_resources_list = list(map(lambda x: x[0], starred_resources_ids))

        starred_resources= ResourceListing.objects.filter(id__in = starred_resources_list).values()
        indexed_starred_resources= {}
        for index, item in enumerate(starred_resources):
            indexed_starred_resources[index] = item
        return JsonResponse({"starred_resources_id" : starred_resources_list, 
                             "starred_resources": indexed_starred_resources})
    return JsonResponse({'error': 'Post request not received'})

@csrf_exempt
def add_star(request):
    if request.method == "POST":
        resourceJSON = json.loads(request.body)
        starred_resource = ResourceListing.objects.get(id = resourceJSON['resourceID'])
        try:  #case when already starred resources is clicked to star, so remove stars
            already_existing_star = StarredResources.objects.get(
                moodleID = resourceJSON['moodleID'],
                resourceID = resourceJSON['resourceID']
            )
            already_existing_star.delete()
            starred_resource.stars = starred_resource.stars - 1;

        except StarredResources.DoesNotExist: #Add starred resource to both tables
            StarredResources.objects.create(
                moodleID = resourceJSON['moodleID'],
                resourceID = resourceJSON['resourceID']
            )
            starred_resource.stars = starred_resource.stars + 1;

        starred_resource.save()

        return JsonResponse({'message': 'Successfully updated resource!'})
    return JsonResponse({'error': 'Post request not received'})

@csrf_exempt
def simple_search(request):
    if request.method == "GET":
        search_term = request.GET.get('searchTerm', '')
        if search_term:
            # Perform the search filtering based on your model
            products = ProductListing.objects.filter(title__icontains=search_term, admin_approval = True)
            # Serialize the products to JSON or obtain necessary data
            serialized_products = [{'id': product.id, 'title': product.title, 'category': product.category,'price': product.price,'selected_year': product.selected_year,'selected_branch': product.selected_branch,'selected_item_type': product.selected_item_type,'selected_condition': product.selected_condition,'product_description': product.product_description, 'image_urls' : product.image_urls, 'admin_approval': product.admin_approval} for product in products]
            return JsonResponse({'filteredProducts': serialized_products})
        else:
            return JsonResponse({'error': 'Search term not provided'}, status=400)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)
