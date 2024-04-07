from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
import json
import razorpay
import os
from .models import Orders

@csrf_exempt
def create_order(request):
    rzp_id = os.getenv('RZP_ID')
    rzp_secret = os.getenv('RZP_SECRET')
    if request.method == "POST":
        productJSON = json.loads(request.body)
        product = productJSON['product']
        client = razorpay.Client(auth=(rzp_id, rzp_secret))
        try:
            order_exists = Orders.objects.get(moodleID = productJSON['moodleID'], productID = productJSON['productId'])
            current_order = client.order.fetch(order_exists.orderID)
        except Orders.DoesNotExist:
            DATA = {
                "amount": product['price'] * 100,
                "currency": "INR",
                "receipt": f"{productJSON['productId']}_{productJSON['moodleID']}",
            }
            current_order = client.order.create(data=DATA)
            Orders.objects.create(moodleID = productJSON['moodleID'], productID = productJSON['productId'], orderID = current_order['id'])
        return JsonResponse({'current_order': current_order})
    return JsonResponse({'error': 'order not sent '})

