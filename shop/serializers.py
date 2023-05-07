from rest_framework import serializers
from .models import Shop, Product, ShopConnector, Cart, CartItems, Category



class ShopSerializer(serializers.ModelSerializer):
    merchant = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Shop
        fields = ('name', 'merchant', 'category')
        read_only_fields = [ 'merchant']
   

class ConnectionRequestSendSerializer(serializers.ModelSerializer):
    # sender = serializers.StringRelatedField(read_only=True)
    # receiver = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = ShopConnector
        fields = ('sender', 'receiver', 'status')

class ConnectionResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShopConnector
        fields = ('status',)

    

class ProductSerializer(serializers.ModelSerializer):
    merchant = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Product
        fields = ('name', 'price', 'shop', 'category', 'merchant', 'image')
        read_only_fields = [ 'merchant']


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ('shop', )
        read_only_fields = ['shop']



class CartItemsSerializer(serializers.ModelSerializer):
    cart = CartSerializer
    product = ProductSerializer
    class Meta:
        model = CartItems
        fields = ('cart','product','quantity')
        read_only_fields = [ 'cart' ]


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('name',)
