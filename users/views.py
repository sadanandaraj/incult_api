import jwt
from django.conf import settings
from django.contrib.auth import authenticate
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser, FileUploadParser
from .models import User
from stores.models import Store
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser, AllowAny
from .permissions import IsSelf
from stores.serializers import StoreSerializer
from .serializers import UserSerializer
from utils import MultipartJsonParser
from rest_framework import parsers


class UsersViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    parser_classes = [MultiPartParser, JSONParser]
    def get_permissions(self):
        if self.action == "list":
            permission_classes = [IsAdminUser]
        elif self.action == "create" or self.action == "retrieve":
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsSelf]
        return [permission() for permission in permission_classes]

    @action(detail=False,methods=["post"])
    def login(self,request):
        username = request.data.get("username")
        password = request.data.get("password")
        if not username or not password:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        user = authenticate(username=username, password=password)
        if user is not None:
            encoded_jwt = jwt.encode({'pk': user.pk}, settings.SECRET_KEY, algorithm='HS256')
            return Response(data={"token": encoded_jwt, "id":user.pk})
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)

    @action(detail=True)
    def following(self, request,pk):
        user = self.get_object()
        serializer = StoreSerializer(user.following_store.all(), many=True).data
        return Response(serializer)

    @following.mapping.put
    def toggle_following(self, request, pk):
        pk = request.data.get("pk",None)
        user = request.user
        if pk is not None:
            try:
                store = Store.objects.get(pk=pk)
                if store in user.following_store.all():
                    user.following_store.remove(store)
                    store.follower.remove(user)
                else:
                    user.following_store.add(store)
                    store.follower.add(user)
                return Response()
            except Store.DoesNotExist:
                pass

        return Response(status=status.HTTP_400_BAD_REQUEST)

