from rest_framework import serializers
from .models import Shop, Product, ShopConnector, Cart, CartItems, Category



class ShopSerializer(serializers.ModelSerializer):
    merchant = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Shop
        fields = ('name', 'merchant', 'category')
        read_only_fields = [ 'merchant']
   

# class ConnectionRequestSendSerializer(serializers.ModelSerializer):
#     # sender = serializers.StringRelatedField(read_only=True)
#     # receiver = serializers.StringRelatedField(read_only=True)
#     class Meta:
#         model = ShopConnector
#         fields = ('sender', 'receiver', 'status')


    

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
    # cart = CartSerializer
    # product = ProductSerializer
    class Meta:
        model = CartItems
        fields = ('cart','product','quantity')
        # read_only_fields = [ 'cart' ]


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('name',)



# class SameCategoryShopField(serializers.PrimaryKeyRelatedField):
#     def validate(self, value):
#         sender = self.context['request'].user
#         shop = Shop.objects.filter(merchant=sender)
#         if sender.category_shop != value.category_shop:
#             raise serializers.ValidationError('The users must have the same category shop.')
#         return value

class ConnectionSerializer(serializers.ModelSerializer):
    #sender = serializers.SerializerMethodField()
    # sender = serializers.PrimaryKeyRelatedField(read_only=True)
    # receiver = SameCategoryShopField(queryset=Shop.objects.all())
    class Meta:
        model = ShopConnector
        fields = ('sender', 'receiver', 'status')

    # def create(self, validated_data):
    #     sender = validated_data.get(sender, None)
    #     receiver = validated_data.get(receiver, None)
    #     if sender.category == receiver.category:
    #         con = Connection.objects.create(**validated_data)
    #     return validated_data

    # def get_sender(self, obj):
    #     #sender = self.context['request'].user
    #     shop = Shop.objects.filter(merchant=self.request.uesr)
    #     return shop
    
    # def validate_receiver(self, value):
    #     sender = self.context['request'].user
    #     if sender != value.category:
    #         raise serializers.ValidationError("The receiving user must have the same category shop as the sending user.")
    #     return value

class ConnectionResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShopConnector
        fields = ('status',)