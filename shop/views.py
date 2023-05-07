from django.shortcuts import render,get_object_or_404
from rest_framework import generics,authentication, permissions

from .serializers import  ShopSerializer, ConnectionRequestSendSerializer, ProductSerializer, CartSerializer, CartItemsSerializer, ConnectionResponseSerializer, CategorySerializer
from . models import Shop, Cart, CartItems, Product, Category
from .permissions import IsShopMerchant, IsShopOwner




class ListCreateCategory(generics.ListCreateAPIView):
    queryset = Category.objects.filter()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAdminUser]


class DetailCategory(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.filter()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAdminUser]
    lookup_field = 'pk'


class CreateShop(generics.CreateAPIView):
    serializer_class = ShopSerializer
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]


class ListMerchantShop(generics.ListAPIView):
    queryset = Shop.objects.filter()
    serializer_class = ShopSerializer
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        return Shop.objects.filter(merchant=self.request.user.id)
    

class RemoveMerchantShop(generics.DestroyAPIView):
    queryset = Shop.objects.filter()
    serializer_class = ShopSerializer
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated, IsShopMerchant]
    lookup_field = 'pk'


class ConnectionRequestSend(generics.CreateAPIView):
    serializer_class = ConnectionRequestSendSerializer
    queryset = Shop.objects.filter()


class ConnectionResponse(generics.CreateAPIView):
    serializer_class = ConnectionResponseSerializer

    def perform_create(self, serializer):
        return serializer.save(status="ACCEPT")


#This comments are future practice

    # def get_queryset(self, **kwargs):
    #     merchant = self.request.user
    #     shop = Shop.objects.filter(merchant=merchant)
    #     #print('shoppppfffffffffffffffffff',shop[0])
    #     #print('qqqqqqqqqqqqqqqqqqq',merchant)
    #     print('eeeeeeeeeeeeeeeeeeeeeeeeee',shop)
    #     return shop

    # def get_object(self):
    #     id = self.kwargs['shop_id']
    #     obj = Shop.objects.get(id=id)
    #     #print('gddddddddddddddddddddddddddddddddddddddddddddddddddsf',obj.category.name)
    #     return obj
        

    # def perform_create(self, serializer):
    #     #print('oooooooooooooooooooooooooooo',self.get_queryset())
    #     for i in list(self.get_queryset()):
    #         print('cheakkkkkkkkkk', type(i.category), type(self.get_object().category.name))
    #         if i == self.get_object().category.name:
    #             print('affffffffffffffffffffffffffter', i, self.get_object().category.name)
    #             return serializer.save(sender=self.shop, receiver=self.obj, status="PENDING")
        

class AddProduct(generics.CreateAPIView):
    queryset = Product.objects.filter()
    serializer_class = ProductSerializer
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]


class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.filter()
    serializer_class = ProductSerializer
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'pk'


class CartListCreate(generics.ListCreateAPIView):
    queryset = Cart.objects.filter()
    serializer_class = CartSerializer
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated,IsShopOwner]


class CartDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cart.objects.filter()
    serializer_class = CartSerializer
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [ IsShopOwner]

    # def get_object(self):
    #     kwargs = {
    #         "shop__id": self.kwargs.get("shop_id", None),
    #         "pk": self.kwargs.get("id", None),
    #     }
    #     return get_object_or_404(Cart, **kwargs)
    
    def get_objects(self):
        pk = self.kwargs['pk']
        obj = Cart.objects.get(pk=pk)
        return obj    

class AddCartItems(generics.CreateAPIView):
    serializer_class = CartItemsSerializer
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated, IsShopOwner]


class CartItemsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = CartItems.objects.filter()
    serializer_class = CartItemsSerializer
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated, IsShopOwner]
   

    # def get_object(self):
    #     kwargs = {
    #         "cart_id": self.kwargs.get("cart_id", None),
    #         "pk": self.kwargs.get("id", None),
    #     }
    #     return get_object_or_404(CartItems, **kwargs)

    def get_objects(self):
        pk = self.kwargs['pk']
        obj = CartItems.objects.get(pk=pk)
        return obj
