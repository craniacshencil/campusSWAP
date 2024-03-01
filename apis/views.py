from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
import json
# Create your views here.
@csrf_exempt
def register(request):
    if request.method == "POST":
        data = json.loads(request.body)
        user = User.objects.create_user(username = data['moodleID'], email = data['email'], password = data['password'],
                                        first_name = data['firstName'], last_name = data['lastName'])
        user.save()
        return JsonResponse(data)
    else:
        return JsonResponse({'error': 'post-request did not reach django'})