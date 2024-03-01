from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
import json
from .models import collegeStudent
# Create your views here.
@csrf_exempt
def register(request):
    if request.method == "POST":
        data = json.loads(request.body)
        error_message = "No Error"
        try:
            is_valid_moodleID = collegeStudent.objects.get(moodleID = data['moodleID']).email
            print(is_valid_moodleID)
        except collegeStudent.DoesNotExist:
            is_valid_moodleID = False
            error_message = "Entered MoodleID is non-existent"

        try:
            is_existing_account = User.objects.get(username = data['moodleID'])
            error_message = "Account for this MoodleID already exists"
        except User.DoesNotExist:
            is_existing_account = False

        #Create account only when
            # i. MoodleId is valid
            # ii. MoodleID and Email match
            # iii. Already account does not exist for MoodleID
            # iv. Confirm password and password match
            # v. Password should be strong
        if is_valid_moodleID and (not is_existing_account) and (data['email'] == is_valid_moodleID) and (data['password'] == data['confirmPassword']) and (data['passwordStrength'] == 'strong'):
            print("Success")
            # user = User.objects.create_user(username = data['moodleID'], email = data['email'], password = data['password'], first_name = data['firstName'], last_name = data['lastName'])
            # user.save()
        else:
            if data['email'] != is_valid_moodleID:
                error_message = "Entered email for the MoodleID is incorrect"
            elif data['password'] != data['confirmPassword']:
                error_message = "Password and Confirm Password don't match"
            elif data['passwordStrength'] != 'strong':
                error_message = "Password is not strong enough\na. It should be atleast 8 characters long\nb. Should include a capital letter\nc. Should include a specail character\nd. Should include a number"
        print(error_message)
        return JsonResponse(data)
    else:
        return JsonResponse({'error': 'post-request did not reach django'})