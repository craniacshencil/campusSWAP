from django.shortcuts import render
from .models import Student
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.

@csrf_exempt  # Disable CSRF protection for simplicity. Ensure to enable it in production.
def save_form_data(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        Student.objects.create(
            moodleid=data.get('moodleID'),
            email=data.get('email'),
            first_name=data.get('firstName'),
            last_name=data.get('lastName'),
            password=data.get('password'),
            # Map other fields accordingly
        )
        return JsonResponse({'message': 'Form data saved successfully'})
    else:
        return JsonResponse({'error': 'Only POST requests are allowed'})
