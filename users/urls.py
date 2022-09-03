from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from users.views import Login, Register , ProfileRetrieveUpdateDestroy , ChangePassword , ValidateOtp 

app_name = "users"


urlpatterns = [
    path("login/", Login.as_view()),
    path("refresh/", TokenRefreshView.as_view()),
    path("register/", Register.as_view()),
    path("profile/<int:pk>/", ProfileRetrieveUpdateDestroy.as_view()),
    path("change_password/<int:pk>/", ChangePassword.as_view()),
    path("validate_otp/", ValidateOtp.as_view()),

]