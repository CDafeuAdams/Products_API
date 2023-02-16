from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import ProductSerializer
from .models import Product

@api_view(['GET', 'POST'])
def all_products(request):
    if request.method == "GET":
        products_list = Product.objects.all()
        serializer = ProductSerializer(products_list, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == "POST":
        serializer = ProductSerializer(data=request.data)
        serializer .is_valid(raise_exception=True)
        serializer .save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
