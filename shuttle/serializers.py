from rest_framework.serializers import ModelSerializer
from shuttle.models import Shuttle, ShuttleReservation

class ShuttleSerializer(ModelSerializer):
    class Meta:
        model = Shuttle
        fields = '__all__'

class ShuttleReservationSerializer(ModelSerializer):
    class Meta:
        model = ShuttleReservation
        fields = '__all__'