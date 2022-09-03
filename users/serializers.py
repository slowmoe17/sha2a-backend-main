from dataclasses import fields
from django.forms import EmailField
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework.serializers import ModelSerializer
from django.contrib.auth.hashers import make_password
from rest_framework import serializers
from users.models import CustomUser , Profile

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = "__all__"
        read_only_fields = ["user"]
        extra_kwargs = {
            "user": {"read_only": True},
        }


class LoginSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        refresh = self.get_token(self.user)

        data["access"] = str(refresh.access_token)
        data["refresh"] = str(refresh)

        data["email"] = self.user.email
        data["is_verified"] = self.user.is_verified

        data["user id"] = self.user.id
        data["username"] = self.user.username

        profile = Profile.objects.get(user=self.user)
        profile_id = profile.id
        data["profile_id"] = profile_id
        
        make_password(self.user.password)

        return data

    


class UserSerializer(ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ["email","phone", "password", "username","is_verified","otp"]

    def create(self, validated_data):
        user = CustomUser(
            email=validated_data["email"],
            phone = validated_data["phone"],          
            username = validated_data["username"],          
            password=make_password(validated_data["password"]),
        )
        
        user.save()
        return user









  