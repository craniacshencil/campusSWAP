from django.http import JsonResponse
import os
import requests
from django.views.decorators.csrf import csrf_exempt
import base64

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
        print(request.body)
        return JsonResponse({'message' : "Succesfully received"})
    return JsonResponse({'error' : 'No post request received'})
