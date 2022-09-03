from rest_framework import serializers
from .models import Property,Favorite

class PropertySerializer(serializers.ModelSerializer):
    class Meta:
        model = Property
        fields = "__all__"
        # read_only_fields = ["user"]
        # extra_kwargs = {
        #     "user": {
        #         "read_only": True
        #     }
        # }

class FavoriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorite
        fields = "__all__"
        read_only_fields = ["user", "property"]
        extra_kwargs = {
            "user": {
                "read_only": True
            },
            "property": {
                "read_only": True
            }
        }