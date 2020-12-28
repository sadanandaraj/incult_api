from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.views import APIView
from rest_framework.decorators import action
from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from rest_framework import status
from .models import Store
from .serializers import StoreSerializer
from .permissions import IsOwner
from products.models import Product
from products.serializers import ProductSerializer

# class OwnPagination(PageNumberPagination):
#     page_size = 20

# class SroresView(APIView):
#     def get(self, request):
#         paginator = OwnPagination()
#         stores = Store.objects.all()
#         results = paginator.paginate_queryset(stores, request)
#         serializer = StoreSerializer(stores,context={"request": request}, many=True)
#         return paginator.get_paginated_response(serializer.data)
        
#     def post(self,request):
#         if not request.user.is_authenticated:
#             return Response(status=status.HTTP_401_UNAUTHORIZED)
#         serializer = StoreSerializer(data=request.data)
#         print(serializer)
#         if serializer.is_valid():
#             store = serializer.save(owner=request.user)
#             store_serializer = StoreSerializer(store).data
#             return Response(data=store_serializer,status=status.HTTP_200_OK)
#         else:
#             return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)


# class StoreView(APIView):

#     def get_store(self, pk):
#         try:
#             store = Store.objects.get(pk=pk)
#             return store
#         except Store.DoesNotExist:
#             return None

#     def get(self, request, pk):
#         store = self.get_store(pk)
#         if store is not None:
#             serializer = StoreSerializer(store,context={"request": request}).data
#             return Response(serializer)
#         else:
#             return Response(status=status.HTTP_404_NOT_FOUND)

#     def put(self,request,pk):
#         store = self.get_store(pk)
#         if store is not None:
#             if store.owner != request.user:
#                 return Response(status=status.HTTP_403_FORBIDDEN)
#             serializer = StoreSerializer(store, data=request.data, partial=True)
#             if serializer.is_valid():
#                 store = serializer.save()
#                 return Response(StoreSerializer(store).data)
#             else:
#                 return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#             return Response()
#         else:
#             return Response(status=status.HTTP_404_NOT_FOUND)

#     def delete(self,request, pk):
#         store = self.get_store(pk)
#         if store.owner != request.user:
#             return Response(status=status.HTTP_403_FORBIDDEN)
#         if store is not None:
#             store.delete()
#             return Response(status=status.HTTP_200_OK)
#         else:
#             return Response(status=status.HTTP_404_NOT_FOUND)

class StoreViewSet(ModelViewSet):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer

    def get_permissions(self):
        if self.action == "list" or self.action == "retrieve" or self.action == "products_detail":
            permission_classes = [permissions.AllowAny]
        elif self.action =="create":
            permission_classes = [permissions.IsAuthenticated]
        else:
            permission_classes = [IsOwner]
        return [permission() for permission in permission_classes]

    @action(detail=False)
    def store_search(self,request):
        name = request.GET.get('name',None)
        description = request.GET.get('description',None)
        offer = request.GET.get('offer',None)
        status = request.GET.get('status',None)
        storeType = request.GET.get('storeType',None)
        lat = request.GET.get("lat",None)
        lng = request.GET.get("lng",None)
        filter_kwargs = {}

        if name is not None:
            filter_kwargs["name"] = name
        if description is not None:
            filter_kwargs["description"] = description
        if offer is not None:
            filter_kwargs["offer"] = offer
        if status is not None:
            filter_kwargs["status"] = status
        if storeType is not None:
            filter_kwargs["storeType"] = storeType
        if lat is not None and lng is not None :
            filter_kwargs["lat__gte"] = float(lat) - 0.005
            filter_kwargs["lat__lte"] = float(lat) + 0.005
            filter_kwargs["lng__gte"] = float(lng) - 0.005
            filter_kwargs["lng__lte"] = float(lng) + 0.005
        paginator = self.paginator
        try:
            store = Store.objects.filter(**filter_kwargs)
        except ValueError:
            store = Store.objects.all()
        results = paginator.paginate_queryset(store, request)
        serializer = StoreSerializer(results, many=True)
        return paginator.get_paginated_response(serializer.data)

    @action(detail=True)
    def products(self, request,pk):
        store = Store.objects.get(pk=pk)
        products = store.products.all()
        serializer = ProductSerializer(products.all(), many=True).data
        return Response(serializer)

    @products.mapping.post
    def add_products(self, request, pk):
        store = Store.objects.get(pk=pk)
        if store.owner == request.user:
            serializer = ProductSerializer(data=request.data)
            if serializer.is_valid():
                product = serializer.save(store=store)
                product_serializer = ProductSerializer(product).data
                return Response(data=product_serializer,status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_403_FORBIDDEN)
