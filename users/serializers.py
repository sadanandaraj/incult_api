from rest_framework import serializers
from .models import User

import base64

from django.core.files.base import ContentFile
from rest_framework import serializers


class Base64ImageField(serializers.ImageField):
    def from_native(self, data):
        if isinstance(data, basestring) and data.startswith('data:image'):
            # base64 encoded image - decode
            format, imgstr = data.split(';base64,')  # format ~= data:image/X,
            ext = format.split('/')[-1]  # guess file extension

            data = ContentFile(base64.b64decode(imgstr), name='temp.' + ext)

        return super(Base64ImageField, self).from_native(data)

class TinySerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("username","avatar")

class UserSerializer(serializers.ModelSerializer):
    avatar = Base64ImageField("avatar")
    password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ("id","username","first_name","last_name","email","avatar","superhost","password")
        read_only_fields = ("id","superhost")
    
    
    def validate(self, data):
        self.context["avatar"] = self.context['request'].FILES.get("avatar")
        print(data)
        return data

    def create(self, validated_data):
        password = validated_data.get('password')
        user = super().create(validated_data)
        user.set_password(password)
        user.save()
        return user