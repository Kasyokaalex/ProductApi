from rest_framework.response import Response
from rest_framework.decorators import api_view
from pvariants.models import Product
from .serializers import ProductSerializer
from rest_framework import status
from rest_framework.views import APIView


@api_view(['GET'])
def getData(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)




@api_view(['POST'])
def bulk_insert_products(request):
    serializer = ProductSerializer(data=request.data, many=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
