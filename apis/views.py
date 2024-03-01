from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
# Create your views here.
@csrf_exempt
def register(request):
    if request.method == "POST":
        print(request.body)
        return JsonResponse({'message': 'post-request successfully reached django'})
    else:
        return JsonResponse({'error': 'post-request did not reach django'})