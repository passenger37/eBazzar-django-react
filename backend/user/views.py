from django.shortcuts import render
from django.http.response import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout


def signup(request):
    fm= UserCreationForm()
    print(fm)
    return HttpResponse(fm)


@api_view(['POST'])
@permission_classes([AllowAny])
def login(request):
    data={}
    username=request.data['username']
    password=request.data['password']
    user=authenticate(username=request.data['username'],password=request.data['password'])
    if user is not None:
        if user.is_active and user.is_authenticated:
            data['messages']='Welcome Hero'
            data['username']=user.username
            data['email']=user.email
            # data['token']=generate_access_token(user)
            login(request, user)
            return Response(data,status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(["GET","POST"])
def logout_user(request):
    logout(request)
    return Response(data={'message': 'User is logged out'}, status=status.HTTP_200_OK)

def profile(request):
    return HttpResponse("Welcome to the Profile Page!")

def reset_password(request):
    return HttpResponse("User Passwor is Resetted!")

def forget_password(request):
    return HttpResponse("Welcome to the Forget Password Page!")

def update_profile(request):
    return HttpResponse("User Profile is Updated!")

def delete_account(request):
    return HttpResponse("User Account is Deleted!")

def update_password(request):
    return HttpResponse("User Password is Updated!")
    

