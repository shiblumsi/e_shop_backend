from django.shortcuts import render,get_object_or_404
from rest_framework import generics,authentication, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import  ShopSerializer, ProductSerializer, CartSerializer, CartItemsSerializer, ConnectionResponseSerializer, CategorySerializer, ConnectionSerializer
from . models import Shop, Cart, CartItems, Product, Category, ShopConnector
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


# class ConnectionRequestSend(generics.CreateAPIView):
#     serializer_class = ConnectionRequestSendSerializer
#     queryset = Shop.objects.filter()



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

    # def get_queryset(self,**kwargs):
    #     product = Product.objects.filter()
    #     CartItems.objects.filter(Product_category=product.catecory)
    #     return super().get_queryset()




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



class ConnectionRequestView(generics.ListCreateAPIView):
    queryset = ShopConnector.objects.all()
    serializer_class = ConnectionSerializer

    

    # def perform_create(self, serializer):
    #     sender = Shop.objects.filter(merchant=self.request.user)
    #     receiver = Shop.objects.filter(merchant=self.request.user).exclude()
    #     return serializer.save(sender=sender,receiver=receiver)

    # def create(self, request, *args, **kwargs):
    #     sender = request.user  # Assuming user authentication is implemented
    #     receiver_id = request.data.get('receiver')  # ID of the user to whom the request is sent
    #     shop_category = request.data.get('shop_category')
    #     shop = Shop.objects.filter(merchant=sender)


    #     # Check if the sender and receiver have the same shop category
    #     receiver_shop = get_object_or_404(Shop, category=shop_category, user_id=receiver_id)

    #     # Create the connection request
    #     connection = Connection(sender=sender, receiver_id=receiver_id, shop_category=shop_category)
    #     connection.save()

    #     return Response({'status': 'Connection request sent'}, status=status.HTTP_201_CREATED)


class ConnectionResponse(generics.CreateAPIView):
    serializer_class = ConnectionResponseSerializer
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        return serializer.save(status="ACCEPT")


class ConnectedShopView(generics.ListAPIView):
    queryset = ShopConnector.objects.filter()
    serializer_class = ConnectionSerializer
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self, **kwargs):
        return ShopConnector.objects.filter(sender_id=self.request.user.id).filter(status="ACCEPT")
    

class ConnectedShopDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ShopConnector.objects.filter()
    serializer_class = ConnectionSerializer
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'pk'


    

        

