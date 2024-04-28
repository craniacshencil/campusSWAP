from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
import json
import razorpay
import os
from .models import Orders, Payments
from products.models import ProductListing 

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

@csrf_exempt
def record_payment(request):
    rzp_id = os.getenv('RZP_ID')
    rzp_secret = os.getenv('RZP_SECRET')
    if request.method == "POST":
        payment_data = json.loads(request.body)
        client = razorpay.Client(auth=(rzp_id, rzp_secret))
        isVerified = client.utility.verify_payment_signature({
            'razorpay_order_id': payment_data['rzp_order_id'],
            'razorpay_payment_id': payment_data['rzp_payment_id'],
            'razorpay_signature': payment_data['rzp_signature']
        })
        productID = Orders.objects.get(orderID = payment_data['rzp_order_id']).productID
        seller_moodle_id = ProductListing.objects.get(id = productID).moodleID
        if(isVerified):
            Payments.objects.create(
                productID = productID,
                buyer_moodleID = payment_data['buyer'],
                orderID = payment_data['rzp_order_id'],
                paymentID = payment_data['rzp_payment_id'],
                transaction_signature = payment_data['rzp_signature'],
                seller_moodleID = seller_moodle_id
            )
        bought_product = ProductListing.objects.get(id = productID)
        bought_product.admin_approval = "sold"
        bought_product.save() #change the status of object to sold so that it doesn't come up on buy page 
        Orders.objects.filter(productID = productID).delete() #delete all orders for the bought product

        return JsonResponse({'verification_status' : isVerified})
    return JsonResponse({'error' : 'failed'})

def get_purchases(request, moodleID):
    if request.method == "GET":
        ids = Payments.objects.filter(buyer_moodleID = moodleID).values_list('productID')
        purchased_products = ProductListing.objects.filter(id__in = ids).values()
        indexed_purchased_products = {}
        for index, item in enumerate(purchased_products):
            indexed_purchased_products[index] = item

        return JsonResponse({"purchasedProducts" : indexed_purchased_products})
    return JsonResponse({"error" : "couldn't send any message sorry"})