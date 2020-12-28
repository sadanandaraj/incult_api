from django.shortcuts import render
from .models import Product
from .serializers import ProductSerializer
from  stores.permissions import IsOwner
from rest_framework.decorators import action
from rest_framework import permissions
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser, AllowAny
from reviews.serializers import ReviewSerializer,ReviewPostSerializer

# Create your views here.
class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_permissions(self):
        if self.action == "list":
            permission_classes = [IsAdminUser]
        elif (self.action == "create"):
            permission_classes = [IsOwner]
        elif (self.action == "retrieve"):
            permission_classes = [AllowAny]
        else:
            permission_classes = [AllowAny]
        return [permission() for permission in permission_classes]

    @action(detail=True)
    def productDetail(self, request,pk):
        if pk is not None:
            try:
                products = Product.objects.get(pk=pk)
                serializer = ProductSerializer(products).data
                return Response(serializer)
            except Product.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

    @productDetail.mapping.put
    def postProduct(self, request,pk):
        products = Product.objects.get(pk=pk)
        print(products.store.owner)
        print(request.user)
        if products.store.owner == request.user:
            serializer = ProductSerializer(products, data=request.data, partial=True)
            if serializer.is_valid():
                products = serializer.save()
                return Response(ProductSerializer(products).data)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)

    @productDetail.mapping.delete
    def DeleteProduct(self, request,pk):
        products = Product.objects.get(pk=pk)
        if products.store.owner == request.user:
            if products is not None:
                products.delete()
                return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)

    @action(detail=True)
    def reviews(self, request,pk):
        product = Product.objects.get(pk=pk)
        reviews = product.reviews.all()
        serializer = ReviewSerializer(reviews.all(), many=True).data
        return Response(serializer)

    @reviews.mapping.post
    def add_review(self, request, pk):
        product = Product.objects.get(pk=pk)
        print(product)
        user = request.user
        print(user)
        serializer = ReviewPostSerializer(data=request.data)
        print(serializer.is_valid)
        if serializer.is_valid():
            review = serializer.save(product=product,user=user)
            review_serializer = ReviewSerializer(review).data
            return Response(data=review_serializer,status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_403_FORBIDDEN)
            
            
        