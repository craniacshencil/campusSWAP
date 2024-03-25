from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
import json
from .models import CollegeStudent, StudentMetaInfo
# Create your views here.
@csrf_exempt
def register(request):
    if request.method == "POST":
        data = json.loads(request.body)
        register_error_message = "No Error"
        register_error_message_json = {
        "register_error" : register_error_message
        }
        try:
            is_valid_moodleID = CollegeStudent.objects.get(moodleID = data['moodleID']).email
        except CollegeStudent.DoesNotExist:
            is_valid_moodleID = False
            register_error_message = "Entered MoodleID is non-existent"
            register_error_message_json = {
            "register_error" : register_error_message
            }
            return JsonResponse(register_error_message_json, safe = False)

        try:
            is_existing_account = User.objects.get(username = data['moodleID'])
            register_error_message = "Account for this MoodleID already exists"
            register_error_message_json = {
            "register_error" : register_error_message
            }
            return JsonResponse(register_error_message_json, safe = False)
        except User.DoesNotExist:
            is_existing_account = False

        #Create account only when
            # i. MoodleId is valid
            # ii. MoodleID and Email match
            # iii. Already account does not exist for MoodleID
            # iv. Confirm password and password match
            # v. Password should be strong
        if is_valid_moodleID and (not is_existing_account) and (data['email'] == is_valid_moodleID) and (data['password'] == data['confirmPassword']) and (data['passwordStrength'] == 'strong'):
            user = User.objects.create_user(username = data['moodleID'], email = data['email'], password = data['password'], first_name = data['firstName'], last_name = data['lastName'])
            user.save()
            StudentMetaInfo.objects.create(moodleID = user, phonenumber = data['phonenumber'])

        else:
            if data['email'] != is_valid_moodleID:
                register_error_message = "Entered email for the MoodleID is incorrect"
            elif data['password'] != data['confirmPassword']:
                register_error_message = "Password and Confirm Password don't match"
            elif data['passwordStrength'] != 'strong':
                register_error_message = "Password is not strong enough"
        register_error_message_json = {
        "register_error" : register_error_message
        }
        return JsonResponse(register_error_message_json, safe = False)
    else:
        return JsonResponse({'error': 'post-request did not reach django'})



@csrf_exempt
def login_page(request):
    if request.method == "POST":
        login_data = json.loads(request.body)
        user = authenticate(request, username = login_data['moodleID'], password = login_data['passText'])
        if user is not None:
            login(request, user)
            login_error = "No Error"
        else:
            try:
                is_existing_account = User.objects.get(username = login_data['moodleID'])
                login_error = "Incorrect password"
            except User.DoesNotExist:
                try:
                    is_valid_moodleID = CollegeStudent.objects.get(moodleID = login_data['moodleID'])
                    login_error = "Account does not exist for entered MoodleID"
                except CollegeStudent.DoesNotExist:
                    login_error = "Invalid MoodleID"
        if(login_error == "No Error"):
            return JsonResponse({
                                    'login_error' : login_error, 
                                    'moodleID': request.user.username,
                                    'first_name': request.user.first_name,
                                    'last_name': request.user.last_name,
                                    'email': request.user.email,
                                    'issuperuser': request.user.is_superuser,
                                }, safe = False)
        else:
            return JsonResponse({
                'login_error': login_error,
            })
    return JsonResponse({"Error" : 'No data reached django'})

@csrf_exempt
def logout_page(request):
    logout(request)
    return JsonResponse({'message' : "Logout-successful"})

@csrf_exempt
def reset_password(request):
    # Errors to check for
    # 1. New pass needs to be strong enough
    # 2. New pass and Confimr pass need to match
    # 3. Old pass doesn't match the original pass
    if request.method == "POST":
        new_pass_error = "No Error"
        passwords = json.loads(request.body)
        user = User.objects.get(username = passwords['moodleID'])
        if not user.check_password(raw_password=passwords['oldPassword']):
            new_pass_error = "This password does not match the old password"
        elif passwords['newPassword'] != passwords['confirmNewPassword']:
            new_pass_error= "Password and Confirm Password don't match"
        elif passwords['passwordStrength'] != 'strong':
            new_pass_error= "Password is not strong enough"
        
        if new_pass_error == "No Error":
            user.set_password(passwords['newPassword'])
            user.save()
        return JsonResponse({'errorMessage' : new_pass_error})
    return JsonResponse({'error' : 'big error'})