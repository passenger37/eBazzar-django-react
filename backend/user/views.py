from django.http.response import HttpResponse
from django.contrib.auth import authenticate,login,logout
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status   
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError

class SignupView(APIView):
    def post(self, request, *args, **kwargs):
        # Extract data
        username = request.data.get("username")
        email = request.data.get("email")
        password = request.data.get("password")

        # Simple validation
        if not username or not email or not password:
            return Response(
                {"detail": "Username, email, and password are required"},
                status=status.HTTP_400_BAD_REQUEST
            )

        # Validate password
        try:
            validate_password(password)
        except ValidationError as e:
            return Response(
                {"detail": " ".join(e.messages)},
                status=status.HTTP_400_BAD_REQUEST
            )

        # Check if user already exists
        if User.objects.filter(username=username).exists():
            return Response(
                {"detail": "Username already exists"},
                status=status.HTTP_400_BAD_REQUEST
            )

        if User.objects.filter(email=email).exists():
            return Response(
                {"detail": "Email already exists"},
                status=status.HTTP_400_BAD_REQUEST
            )

        # Create user
        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        return Response(
            {"detail": "User created"},
            status=status.HTTP_201_CREATED
        )

@api_view(['POST'])
@permission_classes([AllowAny])
def login_user(request):
    data={}
    username=request.data['username']
    password=request.data['password']
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>username.password")
    user=authenticate(request, username=username, password=password)
    if user is not None:
        if user.is_active and user.is_authenticated:
            data['messages']='Welcom Hero'
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
    

