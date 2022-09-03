from django.shortcuts import render
from .models import Shuttle,ShuttleReservation
from rest_framework import generics, permissions, status ,serializers
from rest_framework.response import Response
from .serializers import ShuttleSerializer,ShuttleReservationSerializer
from rest_framework.views import APIView


class ListShuttle(generics.ListAPIView):
    permission_classes = (permissions.AllowAny,)
    queryset = Shuttle.objects.all()
    serializer_class = ShuttleSerializer


class CreateShuttleReservation(generics.CreateAPIView):
    permission_classes = (permissions.AllowAny,)
    queryset = ShuttleReservation.objects.all()
    serializer_class = ShuttleReservationSerializer
    
    def perform_create(self, serializer):
        shuttle = serializer.validated_data.get('shuttle')
        shuttle.seats_booked = shuttle.seats_booked + serializer.validated_data.get('seats_booked')
        shuttle.save()
        serializer.save()
        return Response({"success": "Reservation created successfully."}, status=status.HTTP_201_CREATED)

class DriverShuttlesRequests(APIView):
    permission_classes = (permissions.AllowAny,)
    def get(self, request, *args, **kwargs):
        driver = request.user
        shuttle_requests = Shuttle.objects.filter(driver = driver)
        serializer = ShuttleSerializer(shuttle_requests, many=True)
        return Response(serializer.data)


    