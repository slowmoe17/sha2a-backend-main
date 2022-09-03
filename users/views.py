from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import LoginSerializer, UserSerializer
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework_simplejwt.exceptions import InvalidToken, TokenError
from .models import CustomUser, Profile
from rest_framework.views import APIView
from .permissions import IsOwner
from .serializers import UserProfileSerializer, UserSerializer 

class Login(TokenObtainPairView):
    serializer_class = LoginSerializer
    permission_classes = (permissions.AllowAny,)

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        try:
            user = CustomUser.objects.get(email=request.data["email"])
            if not user.is_verified:
                return Response(
                    {"error": "User is not verified"}, status=status.HTTP_400_BAD_REQUEST
                )
        except CustomUser.DoesNotExist:
            return Response(
                {"error": "User does not exist"}, status=status.HTTP_400_BAD_REQUEST
            )

        if user.is_verified:
    
            try :
            
                serializer.is_valid(raise_exception=True)
                return Response(serializer.validated_data, status=status.HTTP_200_OK)
            except InvalidToken:
                return Response({"detail": "Invalid token"}, status=status.HTTP_400_BAD_REQUEST)
            except TokenError:
                return Response({"detail": "Token error"}, status=status.HTTP_400_BAD_REQUEST)
            
                

        
        

class Register(generics.CreateAPIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    
    def perform_create(self, serializer):
        username = serializer.validated_data.get('username')
        if CustomUser.objects.filter(username = username).count() > 0:
            return Response({"error": "This username is already taken."}, status=status.HTTP_406_NOT_ACCEPTABLE)
        else:
            serializer.save()
            return Response({"success": "User created successfully."}, status=status.HTTP_201_CREATED)
  

    
    
    
    

"""
this view is used to update & get & delete the profile of a user

"""
class ProfileRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Profile.objects.all()
    permission_classes = [IsOwner]
    serializer_class = UserProfileSerializer



    def get(self, request, *args, **kwargs):
        profile = self.get_object()
        serializer = self.serializer_class(profile)
        return Response(serializer.data)

    def put(self, request, *args, **kwargs):
        profile = self.get_object()
        serializer = self.serializer_class(profile, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        profile = self.get_object()
        profile.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ChangePassword(APIView):
    permission_classes = [IsOwner]

    def get_object(self):
        return self.request.user

    def put(self, request, *args, **kwargs):
        user = self.get_object()
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
        

        



class ValidateOtp(APIView):
    permission_classes = (permissions.AllowAny,)

    
    def post(self, request, *args, **kwargs):
        try:
            user = CustomUser.objects.get(email=request.data['email'])
            if user.otp == request.data['otp']:
                user.is_verified = True
                user.save()

               
                
                return Response({"detail": "OTP is valid"}  ,status=status.HTTP_200_OK ,)
            else:
                return Response({"detail": "OTP is invalid"}, status=status.HTTP_400_BAD_REQUEST)
        except CustomUser.DoesNotExist:
            return Response({"detail": "User does not exist"}, status=status.HTTP_400_BAD_REQUEST)
