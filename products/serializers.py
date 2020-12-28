from rest_framework import serializers
from reviews.serializers import ReviewSerializer
from .models import Product,Photo

class Photo2Serializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        exclude = ("product",)

class ProductSerializer(serializers.ModelSerializer):
    photos = Photo2Serializer(many=True,read_only=True)
    class Meta:
        model = Product
        fields = ("id","product_name","quantity","catogary","MRP","selling_price","offer","specs","description","size","colour","photos")
        read_only_fields = ("id","liked")

    def create(self, validated_data):
        request = self.context.get("request")
        return Product.objects.create(**validated_data,)