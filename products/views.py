from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Category, Product, File, Cart
from .serializers import CategorySerializer, ProductSerializer ,FileSerializer

class CategoryListView(APIView):

    def get(self, request):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True, context={'request': request})
        return Response(serializer.data)


class CategoryDetailView(APIView):

    def get(self, request, pk):
        try:
            category = Category.objects.get(pk=pk)
        except Category.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = CategorySerializer(category, context={'request': request})
        return Response(serializer.data)

class ProductListView(APIView):

    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True, context={'request': request})
        return Response(serializer.data)
# Create your views here.

class ProductDetailView(APIView):
    def get(self, request, pk):
        try:
            product = Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = ProductSerializer(product, context={'request': request})
        return Response(serializer.data)

class FileListView(APIView):

    def get(self, request, product_id):
        files = File.objects.filter(product_id=product_id)
        serializer = FileSerializer(files, many=True, context={'request': request})
        return Response(serializer.data)


class FileDetailView(APIView):

    def get(self, request, product_id, pk):
        try:
            f = File.objects.get(pk=pk, product_id=product_id)
        except File.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = FileSerializer(f, context={'request': request})
        return Response(serializer.data)

class CartDetailView(APIView):
    def get(self, request, user_id, pk):
        try:
            cart = Cart.objects.get(pk=pk, user_id=user_id)
        except cart.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = Cart(cart, context={'request': request})
        return Response(serializer.data)