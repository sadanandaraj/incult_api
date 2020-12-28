from django.shortcuts import render
from .models import Review
from .serializers import ReviewSerializer
from  stores.permissions import IsOwner
from rest_framework.decorators import action
from rest_framework import permissions
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser, AllowAny


# Create your views here.
class ReviewViewSet(ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

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
    def reviewDetail(self, request,pk):
        if pk is not None:
            try:
                review = Review.objects.get(pk=pk)
                serializer = ReviewSerializer(review).data
                return Response(serializer)
            except Review.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

    @reviewDetail.mapping.put
    def postReview(self, request,pk):
        review = Review.objects.get(pk=pk)
        print(review.user)
        print(request.user)
        if review.user == request.user:
            serializer = ReviewSerializer(review, data=request.data, partial=True)
            if serializer.is_valid():
                review = serializer.save()
                return Response(ReviewSerializer(review).data)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)

    @reviewDetail.mapping.delete
    def DeleteReview(self, request,pk):
        review = Review.objects.get(pk=pk)
        if review.user == request.user:
            if review is not None:
                review.delete()
                return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)

