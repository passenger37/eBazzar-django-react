from django.urls import path
from .views import (profile,
                    signup,
                    login,
                    logout_user,
                    reset_password,
                    forget_password,
                    update_profile,
                    delete_account,
                    update_password)

app_name=('user')
urlpatterns = [
    path('signup/', signup, name='signup'),
    path('login/', login, name='login'),
    path('logout/', logout_user, name='logout'),
    path('profile/', profile, name='profile'),
    path('resetpassword/', reset_password, name='logout'),
    path('forgetpassword/', forget_password, name='forget_password'),
    path('updateprofile/', update_profile, name='update_profile'),
    path('deleteaccount/', delete_account, name='delete_account'),
    path("update_password/", update_password, name="update_password")
]
