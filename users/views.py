from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import LoginSerializer, UserSerializer
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework_simplejwt.exceptions import InvalidToken, TokenError
from .models import CustomUser
from rest_framework.views import APIView
from .serializers import  UserSerializer 

class Login(TokenObtainPairView):
    serializer_class = LoginSerializer
    permission_classes = (permissions.AllowAny,)

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

       
    
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
  

    
    
    
    



