from rest_framework import serializers
from users.serializers import TinySerializer
from products.serializers import ProductSerializer
from .models import Store,StoreType

class StoreSerializer(serializers.ModelSerializer):
    # storeType = StoreTypeSerializer()
    # products = ProductSerializer(many=True)
    owner = TinySerializer(read_only=True)
    is_following = serializers.SerializerMethodField()
    class Meta:
       model = Store
       exclude = ("modified",)
       read_only_fields = ('user','id','created','updated',"follower")

    def create(self, validated_data):
        request = self.context.get("request")
        return Store.objects.create(**validated_data,owner=request.user)

    def get_is_following(self, obj):
        request = self.context.get('request')
        if request:
            user = request.user
            if user.is_authenticated:
                return obj in user.following_store.all()
        return False

       







