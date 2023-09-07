from rest_framework import serializers

from .models import Category, Product ,File, Cart

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('title', 'description', 'avatar')


class FileSerializer(serializers.ModelSerializer):

    class Meta:
        model = File
        fields = ('id', 'title', 'file')


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    categories = CategorySerializer(many=True)
    files = FileSerializer(many=True)
    class Meta:
        model = Product
        fields = ('id','title', 'price', 'quantity', 'description', 'avatar', 'categories','files','url')

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ('product', 'user', 'created_at')
class AddToCartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id')