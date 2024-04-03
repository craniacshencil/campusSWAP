from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
import json
import razorpay
import os

@csrf_exempt
def create_order(request):
    productIdJSON = json.loads(request.body)
    rzp_id = os.getenv('RZP_ID')
    rzp_secret = os.getenv('RZP_SECRET')
    if request.method == "POST":
        client = razorpay.Client(auth=(rzp_id, rzp_secret))
        DATA = {
            "amount": 100,
            "currency": "INR",
            "receipt": productIdJSON['productId'],
        }
        response = client.order.create(data=DATA)
        print(response)
        return JsonResponse({'message': 'order sent'})
    return JsonResponse({'error': 'order not sent '})