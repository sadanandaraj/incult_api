from rest_framework import serializers
from users.serializers import TinySerializer
from .models import Review



class ReviewSerializer(serializers.ModelSerializer):
    user = TinySerializer(read_only=True)
    class Meta:
        model = Review
        fields = ("id","review","accuracy","quality","communication","cleanliness","location","value","user","product")
        read_only_fields = ("id",)

    def create(self, validated_data):
        request = self.context.get("request")
        return Review.objects.create(**validated_data,)

class ReviewPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ("id","review","accuracy","quality","communication","cleanliness","location","value")
        read_only_fields = ("id",)

    def create(self, validated_data):
        request = self.context.get("request")
        return Review.objects.create(**validated_data,)

# class ReviewDetailSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Review
#         fields = ("id","review","accuracy","quality","communication","cleanliness","location","value","user","product")
#         read_only_fields = ("id",)

#     def create(self, validated_data):
#         request = self.context.get("request")
#         return Review.objects.create(**validated_data,)